from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


def assert_file_create_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(actual=response.file.filename, expected=request.filename, name="filename")
    assert_equal(actual=response.file.directory, expected=request.directory, name="directory")
    assert_is_true(actual=response.file.id, name="id")
    assert_equal(actual=str(response.file.url), expected=expected_url, name="url")

def assert_file(actual: FileSchema, expected: FileSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")

def assert_get_file_response(create_file_response: CreateFileResponseSchema, get_file_response: GetFileResponseSchema):
    assert_file(create_file_response.file, get_file_response.file)