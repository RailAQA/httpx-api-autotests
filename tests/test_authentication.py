from clients.authentification.authentification_client import AuthentificationClient
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from tests.conftest import UserFixture
from tools.assertions.authentification import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

from http import HTTPStatus


def test_login(function_user: UserFixture, authentification_client: AuthentificationClient):
    login_user_request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )
    login_response = authentification_client.login_api(request=login_user_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(actual=login_response.status_code, expected=HTTPStatus.OK)
    assert_login_response(response=login_response_data)
    validate_json_schema(instance=login_response.json(), schema=login_response_data.model_json_schema())