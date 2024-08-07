# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementRestorePointsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create(self, resource_group):
        response = self.client.restore_points.begin_create(
            resource_group_name=resource_group.name,
            restore_point_collection_name="str",
            restore_point_name="str",
            parameters={
                "consistencyMode": "str",
                "excludeDisks": [{"id": "str"}],
                "id": "str",
                "name": "str",
                "provisioningState": "str",
                "sourceMetadata": {
                    "diagnosticsProfile": {"bootDiagnostics": {"enabled": bool, "storageUri": "str"}},
                    "hardwareProfile": {"vmSize": "str"},
                    "licenseType": "str",
                    "location": "str",
                    "osProfile": {
                        "adminPassword": "str",
                        "adminUsername": "str",
                        "allowExtensionOperations": bool,
                        "computerName": "str",
                        "customData": "str",
                        "linuxConfiguration": {
                            "disablePasswordAuthentication": bool,
                            "patchSettings": {"assessmentMode": "str", "patchMode": "str"},
                            "provisionVMAgent": bool,
                            "ssh": {"publicKeys": [{"keyData": "str", "path": "str"}]},
                        },
                        "requireGuestProvisionSignal": bool,
                        "secrets": [
                            {
                                "sourceVault": {"id": "str"},
                                "vaultCertificates": [{"certificateStore": "str", "certificateUrl": "str"}],
                            }
                        ],
                        "windowsConfiguration": {
                            "additionalUnattendContent": [
                                {
                                    "componentName": "Microsoft-Windows-Shell-Setup",
                                    "content": "str",
                                    "passName": "OobeSystem",
                                    "settingName": "str",
                                }
                            ],
                            "enableAutomaticUpdates": bool,
                            "patchSettings": {"assessmentMode": "str", "enableHotpatching": bool, "patchMode": "str"},
                            "provisionVMAgent": bool,
                            "timeZone": "str",
                            "winRM": {"listeners": [{"certificateUrl": "str", "protocol": "str"}]},
                        },
                    },
                    "securityProfile": {
                        "encryptionAtHost": bool,
                        "securityType": "str",
                        "uefiSettings": {"secureBootEnabled": bool, "vTpmEnabled": bool},
                    },
                    "storageProfile": {
                        "dataDisks": [
                            {
                                "caching": "str",
                                "diskRestorePoint": {"id": "str"},
                                "diskSizeGB": 0,
                                "lun": 0,
                                "managedDisk": {
                                    "diskEncryptionSet": {"id": "str"},
                                    "id": "str",
                                    "storageAccountType": "str",
                                },
                                "name": "str",
                            }
                        ],
                        "osDisk": {
                            "caching": "str",
                            "diskRestorePoint": {"id": "str"},
                            "diskSizeGB": 0,
                            "encryptionSettings": {
                                "diskEncryptionKey": {"secretUrl": "str", "sourceVault": {"id": "str"}},
                                "enabled": bool,
                                "keyEncryptionKey": {"keyUrl": "str", "sourceVault": {"id": "str"}},
                            },
                            "managedDisk": {
                                "diskEncryptionSet": {"id": "str"},
                                "id": "str",
                                "storageAccountType": "str",
                            },
                            "name": "str",
                            "osType": "str",
                        },
                    },
                    "vmId": "str",
                },
                "timeCreated": "2020-02-20 00:00:00",
                "type": "str",
            },
            api_version="2021-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.restore_points.begin_delete(
            resource_group_name=resource_group.name,
            restore_point_collection_name="str",
            restore_point_name="str",
            api_version="2021-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.restore_points.get(
            resource_group_name=resource_group.name,
            restore_point_collection_name="str",
            restore_point_name="str",
            api_version="2021-03-01",
        )

        # please add some check logic here by yourself
        # ...
