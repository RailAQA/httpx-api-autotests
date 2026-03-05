from http import HTTPStatus
import pytest

from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.assertions.files import assert_file_create_response, assert_get_file_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from clients.files.files_client import FileClient


class TestFile:
    def test_create_file(self, files_client: FileClient):
        request = CreateFileRequestSchema(upload_file="testdata/files/image.png")
        response = files_client.create_file_api(request=request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_file_create_response(request=request, response=response_data)

    def test_get_file(self, files_client: FileClient, function_file: FileFixture):
        response = files_client.get_file_api(file_id=function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)
        
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_get_file_response(function_file.response, response_data)