from pydantic import BaseModel
import pytest

from clients.files.files_client import FileClient, get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.authentification import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def files_client(function_user: UserFixture) -> FileClient:
    return get_private_files_client(function_user.authentification_user)

@pytest.fixture
def function_file(files_client: FileClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file=".testdata/files/image.png")
    response = files_client.create_file(request=request)
    return FileFixture(request=request, response=response)