# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class AzureEntityResource(Resource):
    """The resource model definition for an Azure Resource Manager resource with an etag.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.SystemData
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "etag": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "etag": {"key": "etag", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.etag = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details:
     list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class Fleet(TrackedResource):
    """The Fleet resource which contains multiple Kubernetes clusters as its members.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    :ivar hub_profile: The FleetHubProfile configures the Fleet's hub.
    :vartype hub_profile:
     ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetHubProfile
    :ivar provisioning_state: The provisioning state of the last accepted operation. Known values
     are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating".
    :vartype provisioning_state: str or
     ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetProvisioningState
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "etag": {"readonly": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "etag": {"key": "etag", "type": "str"},
        "hub_profile": {"key": "properties.hubProfile", "type": "FleetHubProfile"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        hub_profile: Optional["_models.FleetHubProfile"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword hub_profile: The FleetHubProfile configures the Fleet's hub.
        :paramtype hub_profile:
         ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetHubProfile
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.etag = None
        self.hub_profile = hub_profile
        self.provisioning_state = None


class FleetCredentialResult(_serialization.Model):
    """The credential result response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the credential.
    :vartype name: str
    :ivar value: Base64-encoded Kubernetes configuration file.
    :vartype value: bytes
    """

    _validation = {
        "name": {"readonly": True},
        "value": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "value": {"key": "value", "type": "bytearray"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.name = None
        self.value = None


class FleetCredentialResults(_serialization.Model):
    """The list credential result response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar kubeconfigs: Base64-encoded Kubernetes configuration file.
    :vartype kubeconfigs:
     list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetCredentialResult]
    """

    _validation = {
        "kubeconfigs": {"readonly": True},
    }

    _attribute_map = {
        "kubeconfigs": {"key": "kubeconfigs", "type": "[FleetCredentialResult]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.kubeconfigs = None


class FleetHubProfile(_serialization.Model):
    """The FleetHubProfile configures the fleet hub.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar dns_prefix: DNS prefix used to create the FQDN for the Fleet hub.
    :vartype dns_prefix: str
    :ivar fqdn: The FQDN of the Fleet hub.
    :vartype fqdn: str
    :ivar kubernetes_version: The Kubernetes version of the Fleet hub.
    :vartype kubernetes_version: str
    """

    _validation = {
        "fqdn": {"readonly": True},
        "kubernetes_version": {"readonly": True},
    }

    _attribute_map = {
        "dns_prefix": {"key": "dnsPrefix", "type": "str"},
        "fqdn": {"key": "fqdn", "type": "str"},
        "kubernetes_version": {"key": "kubernetesVersion", "type": "str"},
    }

    def __init__(self, *, dns_prefix: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword dns_prefix: DNS prefix used to create the FQDN for the Fleet hub.
        :paramtype dns_prefix: str
        """
        super().__init__(**kwargs)
        self.dns_prefix = dns_prefix
        self.fqdn = None
        self.kubernetes_version = None


class FleetListResult(_serialization.Model):
    """The response from the List Fleets operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The list of Fleets.
    :vartype value: list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.Fleet]
    :ivar next_link: The URL to get the next page of Fleets.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Fleet]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.Fleet"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: The list of Fleets.
        :paramtype value: list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.Fleet]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class FleetMember(AzureEntityResource):
    """A member of the Fleet. It contains a reference to an existing Kubernetes cluster on Azure.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.SystemData
    :ivar etag: Resource Etag.
    :vartype etag: str
    :ivar cluster_resource_id: The ARM resource id of the cluster that joins the Fleet. Must be a
     valid Azure resource id. e.g.:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{clusterName}'.  # pylint: disable=line-too-long
    :vartype cluster_resource_id: str
    :ivar provisioning_state: The provisioning state of the last accepted operation. Known values
     are: "Succeeded", "Failed", "Canceled", "Joining", "Leaving", and "Updating".
    :vartype provisioning_state: str or
     ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetMemberProvisioningState
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "etag": {"readonly": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "etag": {"key": "etag", "type": "str"},
        "cluster_resource_id": {"key": "properties.clusterResourceId", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(self, *, cluster_resource_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword cluster_resource_id: The ARM resource id of the cluster that joins the Fleet. Must be
         a valid Azure resource id. e.g.:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{clusterName}'.  # pylint: disable=line-too-long
        :paramtype cluster_resource_id: str
        """
        super().__init__(**kwargs)
        self.cluster_resource_id = cluster_resource_id
        self.provisioning_state = None


class FleetMembersListResult(_serialization.Model):
    """The response from the List FleetMembers operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The list of members in a given Fleet.
    :vartype value: list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetMember]
    :ivar next_link: The URL to get the next page of Fleet members.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[FleetMember]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.FleetMember"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: The list of members in a given Fleet.
        :paramtype value:
         list[~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.FleetMember]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class FleetPatch(_serialization.Model):
    """Properties of a Fleet that can be patched.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.tags = tags


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or
     ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or
         ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or
         ~azure.mgmt.containerservicefleet.v2022_07_02_preview.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
