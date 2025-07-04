# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import logging
import os

from typing import Dict, Optional, Union, Any

from opentelemetry.environment_variables import OTEL_METRICS_EXPORTER
from opentelemetry.util.types import Attributes
from opentelemetry.sdk.environment_variables import OTEL_EXPORTER_OTLP_METRICS_ENDPOINT
from opentelemetry.sdk.metrics import (
    Counter,
    Histogram,
    ObservableCounter,
    ObservableGauge,
    ObservableUpDownCounter,
    UpDownCounter,
)
from opentelemetry.sdk.metrics.export import (
    AggregationTemporality,
    DataPointT,
    HistogramDataPoint,
    MetricExporter,
    MetricExportResult,
    MetricsData as OTMetricsData,
    NumberDataPoint,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util.instrumentation import InstrumentationScope
from opentelemetry.semconv.attributes.http_attributes import HTTP_RESPONSE_STATUS_CODE
from opentelemetry.semconv.metrics import MetricInstruments
from opentelemetry.semconv.metrics.http_metrics import (
    HTTP_CLIENT_REQUEST_DURATION,
    HTTP_SERVER_REQUEST_DURATION,
)
from opentelemetry.semconv.trace import SpanAttributes

from azure.monitor.opentelemetry.exporter._constants import (
    _APPLICATIONINSIGHTS_METRICS_TO_LOGANALYTICS_ENABLED,
    _APPLICATIONINSIGHTS_METRIC_NAMESPACE_OPT_IN,
    _AUTOCOLLECTED_INSTRUMENT_NAMES,
    _METRIC_ENVELOPE_NAME,
)
from azure.monitor.opentelemetry.exporter import _utils
from azure.monitor.opentelemetry.exporter._generated.models import (
    ContextTagKeys,
    MetricDataPoint,
    MetricsData,
    MonitorBase,
    TelemetryItem,
)
from azure.monitor.opentelemetry.exporter.export._base import (
    BaseExporter,
    ExportResult,
)
from azure.monitor.opentelemetry.exporter.export.trace import _utils as trace_utils


_logger = logging.getLogger(__name__)

__all__ = ["AzureMonitorMetricExporter"]


APPLICATION_INSIGHTS_METRIC_TEMPORALITIES = {
    Counter: AggregationTemporality.DELTA,
    Histogram: AggregationTemporality.DELTA,
    ObservableCounter: AggregationTemporality.DELTA,
    ObservableGauge: AggregationTemporality.CUMULATIVE,
    ObservableUpDownCounter: AggregationTemporality.CUMULATIVE,
    UpDownCounter: AggregationTemporality.CUMULATIVE,
}


class AzureMonitorMetricExporter(BaseExporter, MetricExporter):
    """Azure Monitor Metric exporter for OpenTelemetry."""

    def __init__(self, **kwargs: Any) -> None:
        BaseExporter.__init__(self, **kwargs)
        MetricExporter.__init__(
            self,
            preferred_temporality=APPLICATION_INSIGHTS_METRIC_TEMPORALITIES,  # type: ignore
            preferred_aggregation=kwargs.get("preferred_aggregation"),  # type: ignore
        )
        self._metrics_to_log_analytics = self._determine_metrics_to_log_analytics()

    # pylint: disable=R1702
    def export(
        self,
        metrics_data: OTMetricsData,
        timeout_millis: float = 10_000,
        **kwargs: Any,
    ) -> MetricExportResult:
        """Exports a batch of metric data

        :param metrics_data: OpenTelemetry Metric(s) to export.
        :type metrics_data: Sequence[~opentelemetry.sdk.metrics._internal.point.MetricsData]
        :param timeout_millis: The maximum amount of time to wait for each export. Not currently used.
        :type timeout_millis: float
        :return: The result of the export.
        :rtype: ~opentelemetry.sdk.metrics.export.MetricExportResult
        """
        envelopes = []
        if metrics_data is None:
            return MetricExportResult.SUCCESS
        for resource_metric in metrics_data.resource_metrics:
            for scope_metric in resource_metric.scope_metrics:
                for metric in scope_metric.metrics:
                    for point in metric.data.data_points:
                        if point is not None:
                            envelope = self._point_to_envelope(
                                point,
                                metric.name,
                                resource_metric.resource,
                                scope_metric.scope,
                            )
                            if envelope is not None:
                                envelopes.append(envelope)
        try:
            result = self._transmit(envelopes)
            self._handle_transmit_from_storage(envelopes, result)
            return _get_metric_export_result(result)
        except Exception:  # pylint: disable=broad-except
            _logger.exception("Exception occurred while exporting the data.")  # pylint: disable=C4769
            return _get_metric_export_result(ExportResult.FAILED_NOT_RETRYABLE)

    def force_flush(
        self,
        timeout_millis: float = 10_000,
    ) -> bool:
        # Ensure that export of any metrics currently received by the exporter are completed as soon as possible.

        return True

    def shutdown(
        self,
        timeout_millis: float = 30_000,
        **kwargs: Any,
    ) -> None:
        """Shuts down the exporter.

        Called when the SDK is shut down.

        :param timeout_millis: The maximum amount of time to wait for shutdown. Not currently used.
        :type timeout_millis: float
        """
        if self.storage:
            self.storage.close()

    # pylint: disable=protected-access
    def _point_to_envelope(
        self,
        point: DataPointT,
        name: str,
        resource: Optional[Resource] = None,
        scope: Optional[InstrumentationScope] = None,
    ) -> Optional[TelemetryItem]:
        # When Metrics to Log Analytics is disabled, only send Standard metrics and _OTELRESOURCE_
        if not self._metrics_to_log_analytics and name not in _AUTOCOLLECTED_INSTRUMENT_NAMES:
            return None
        envelope = _convert_point_to_envelope(point, name, resource, scope)
        if name in _AUTOCOLLECTED_INSTRUMENT_NAMES:
            envelope = _handle_std_metric_envelope(envelope, name, point.attributes)  # type: ignore
        if envelope is not None:
            envelope.instrumentation_key = self._instrumentation_key
            # Only set SentToAMW on AKS Attach
            if _utils._is_on_aks() and _utils._is_attach_enabled() and not self._is_stats_exporter():
                if (
                    OTEL_EXPORTER_OTLP_METRICS_ENDPOINT in os.environ
                    and "otlp" in os.environ.get(OTEL_METRICS_EXPORTER, "")
                ):
                    envelope.data.base_data.properties["_MS.SentToAMW"] = "True"  # type: ignore
                else:
                    envelope.data.base_data.properties["_MS.SentToAMW"] = "False"  # type: ignore

        return envelope

    # pylint: disable=protected-access
    def _determine_metrics_to_log_analytics(self) -> bool:
        """
        Determines whether metrics should be sent to Log Analytics.

        :return: False if metrics should not be sent to Log Analytics, True otherwise.
        :rtype: bool
        """
        # Disabling metrics to Log Analytics via env var is currently only specified for AKS Attach scenarios.
        if not _utils._is_on_aks() or not _utils._is_attach_enabled() or self._is_stats_exporter():
            return True
        env_var = os.environ.get(_APPLICATIONINSIGHTS_METRICS_TO_LOGANALYTICS_ENABLED)
        if not env_var:
            return True
        return env_var.lower().strip() != "false"

    # pylint: disable=docstring-keyword-should-match-keyword-only
    @classmethod
    def from_connection_string(cls, conn_str: str, **kwargs: Any) -> "AzureMonitorMetricExporter":
        """
        Create an AzureMonitorMetricExporter from a connection string. This is
        the recommended way of instantiation if a connection string is passed in
        explicitly. If a user wants to use a connection string provided by
        environment variable, the constructor of the exporter can be called
        directly.

        :param str conn_str: The connection string to be used for
            authentication.
        :keyword str api_version: The service API version used. Defaults to
            latest.
        :return: An instance of ~AzureMonitorMetricExporter
        :rtype: ~azure.monitor.opentelemetry.exporter.AzureMonitorMetricExporter
        """
        return cls(connection_string=conn_str, **kwargs)


# pylint: disable=protected-access
def _convert_point_to_envelope(
    point: DataPointT, name: str, resource: Optional[Resource] = None, scope: Optional[InstrumentationScope] = None
) -> TelemetryItem:
    envelope = _utils._create_telemetry_item(point.time_unix_nano)
    envelope.name = _METRIC_ENVELOPE_NAME
    envelope.tags.update(_utils._populate_part_a_fields(resource))  # type: ignore
    if _utils._is_any_synthetic_source(point.attributes):
        envelope.tags[ContextTagKeys.AI_OPERATION_SYNTHETIC_SOURCE] = "True"  # type: ignore
    namespace = None
    if scope is not None and _is_metric_namespace_opted_in():
        namespace = str(scope.name)[:256]
    value: Union[int, float] = 0
    count = 1
    min_ = None
    max_ = None
    # std_dev = None

    if isinstance(point, NumberDataPoint):
        value = point.value
    elif isinstance(point, HistogramDataPoint):
        value = point.sum
        count = int(point.count)
        min_ = point.min
        max_ = point.max

    # truncation logic
    properties = _utils._filter_custom_properties(point.attributes)

    data_point = MetricDataPoint(
        name=str(name)[:1024],
        namespace=namespace,
        value=value,
        count=count,
        min=min_,
        max=max_,
    )

    data = MetricsData(
        properties=properties,
        metrics=[data_point],
    )

    envelope.data = MonitorBase(base_data=data, base_type="MetricData")

    return envelope


def _handle_std_metric_envelope(
    envelope: TelemetryItem,
    name: str,
    attributes: Attributes,
) -> Optional[TelemetryItem]:
    properties: Dict[str, str] = {}
    tags = envelope.tags
    if not attributes:
        attributes = {}
    status_code = attributes.get(HTTP_RESPONSE_STATUS_CODE) or attributes.get(SpanAttributes.HTTP_STATUS_CODE)
    if status_code:
        try:
            status_code = int(status_code)  # type: ignore
        except ValueError:
            status_code = 0
    else:
        status_code = 0
    if name in (HTTP_CLIENT_REQUEST_DURATION, MetricInstruments.HTTP_CLIENT_DURATION):
        properties["_MS.MetricId"] = "dependencies/duration"
        properties["_MS.IsAutocollected"] = "True"
        properties["Dependency.Type"] = "http"
        properties["Dependency.Success"] = str(_is_status_code_success(status_code))  # type: ignore
        target, _ = trace_utils._get_target_and_path_for_http_dependency(attributes)
        properties["dependency/target"] = target  # type: ignore
        properties["dependency/resultCode"] = str(status_code)
        properties["cloud/roleInstance"] = tags["ai.cloud.roleInstance"]  # type: ignore
        properties["cloud/roleName"] = tags["ai.cloud.role"]  # type: ignore
    elif name in (HTTP_SERVER_REQUEST_DURATION, MetricInstruments.HTTP_SERVER_DURATION):
        properties["_MS.MetricId"] = "requests/duration"
        properties["_MS.IsAutocollected"] = "True"
        properties["request/resultCode"] = str(status_code)
        # TODO: Change to symbol once released in upstream
        if attributes.get("user_agent.synthetic.type"):
            properties["operation/synthetic"] = "True"
        properties["cloud/roleInstance"] = tags["ai.cloud.roleInstance"]  # type: ignore
        properties["cloud/roleName"] = tags["ai.cloud.role"]  # type: ignore
        properties["Request.Success"] = str(_is_status_code_success(status_code))  # type: ignore
    else:
        # Any other autocollected metrics are not supported yet for standard metrics
        # We ignore these envelopes in these cases
        return None

    # TODO: rpc, database, messaging

    envelope.data.base_data.properties = properties  # type: ignore

    return envelope


def _is_status_code_success(status_code: Optional[str]) -> bool:
    if status_code is None or status_code == 0:
        return False
    try:
        # Success criteria based solely off status code is True only if status_code < 400
        # for both client and server spans
        return int(status_code) < 400
    except ValueError:
        return False


def _is_metric_namespace_opted_in() -> bool:
    return os.environ.get(_APPLICATIONINSIGHTS_METRIC_NAMESPACE_OPT_IN, "False").lower() == "true"


def _get_metric_export_result(result: ExportResult) -> MetricExportResult:
    if result == ExportResult.SUCCESS:
        return MetricExportResult.SUCCESS
    return MetricExportResult.FAILURE
