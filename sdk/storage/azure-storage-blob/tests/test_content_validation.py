# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from io import BytesIO

import pytest
from azure.storage.blob import (
    BlobBlock,
    BlobServiceClient,
    ContainerClient
)

from devtools_testutils import recorded_by_proxy
from devtools_testutils.storage import StorageRecordedTestCase
from settings.testcase import BlobPreparer


class TestStorageContentValidation(StorageRecordedTestCase):
    bsc: BlobServiceClient = None
    container: ContainerClient = None

    def _setup(self, account_name, account_key):
        self.bsc = BlobServiceClient(self.account_url(account_name, "blob"), credential=account_key, logging_enable=True)
        self.container = self.bsc.get_container_client(self.get_resource_name('utcontainer'))
        self.container.create_container()

    def teardown_method(self, _):
        if self.container:
            try:
                self.container.delete_container()
            except:
                pass

    def _get_blob_reference(self):
        return self.get_resource_name('blob')

    @BlobPreparer()
    @recorded_by_proxy
    def test_stage_block(self, **kwargs):
        storage_account_name = kwargs.pop("storage_account_name")
        storage_account_key = kwargs.pop("storage_account_key")

        self._setup(storage_account_name, storage_account_key)
        blob = self.container.get_blob_client(self._get_blob_reference())
        data1 = b'abc' * 512
        data2 = b'123' * 512
        data3 = '你好世界' * 10

        # Act
        blob.stage_block('1', data1, validate_content='crc64')
        blob.stage_block('2', data2, validate_content='crc64')
        blob.stage_block('3', data3, encoding='utf-8-sig', validate_content='crc64')
        blob.commit_block_list([BlobBlock('1'), BlobBlock('2'), BlobBlock('3')])

        # Assert
        content = blob.download_blob()
        assert content.readall() == data1 + data2 + data3.encode('utf-8-sig')

    @pytest.mark.live_test_only
    @BlobPreparer()
    def test_stage_block_large(self, **kwargs):
        storage_account_name = kwargs.pop("storage_account_name")
        storage_account_key = kwargs.pop("storage_account_key")

        self._setup(storage_account_name, storage_account_key)
        blob = self.container.get_blob_client(self._get_blob_reference())
        data1 = b'abcde' * 1024 * 1024  # 5 MiB
        data2 = b'12345' * 1024 * 1024 * 2 + b'abcdefg'  # 10 MiB + 7

        # Act
        blob.stage_block('1', data1, validate_content='crc64')
        blob.stage_block('2', data2, validate_content='crc64')
        blob.commit_block_list([BlobBlock('1'), BlobBlock('2')])

        # Assert
        content = blob.download_blob()
        assert content.readall() == data1 + data2

    @BlobPreparer()
    @recorded_by_proxy
    def test_stage_block_data_types(self, **kwargs):
        storage_account_name = kwargs.pop("storage_account_name")
        storage_account_key = kwargs.pop("storage_account_key")

        self._setup(storage_account_name, storage_account_key)
        blob = self.container.get_blob_client(self._get_blob_reference())

        content = b'abcde' * 1030  # 5 KiB + 30
        byte_io = BytesIO(content)

        def generator():
            for i in range(0, len(content), 500):
                yield content[i: i + 500]

        # TODO: Fix Iterable[str]? (Or just require length)
        # def text_generator():
        #     s_content = str(content, encoding='utf-8')
        #     for i in range(0, len(s_content), 500):
        #         yield s_content[i: i + 500]

        data_list = [byte_io, generator()]

        blocks = []
        for j in range(len(data_list)):
            blob.stage_block(str(j), data_list[j], validate_content='crc64')
            blocks.append(BlobBlock(str(j)))
        blob.commit_block_list(blocks)

        # Assert
        result = blob.download_blob()
        assert result.readall() == content * 2

    @BlobPreparer()
    @recorded_by_proxy
    def test_stage_block_length_specified(self, **kwargs):
        storage_account_name = kwargs.pop("storage_account_name")
        storage_account_key = kwargs.pop("storage_account_key")

        self._setup(storage_account_name, storage_account_key)
        blob = self.container.get_blob_client(self._get_blob_reference())

        content = b'abcde' * 1030  # 5 KiB + 30
        byte_io = BytesIO(content)

        # Specify length less than total length
        blob.stage_block('1', content, length=2000, validate_content='crc64')
        blob.stage_block('2', byte_io, length=2000, validate_content='crc64')
        blob.commit_block_list([BlobBlock('1'), BlobBlock('2')])

        # Assert
        result = blob.download_blob()
        assert result.readall() == content[:2000] * 2
