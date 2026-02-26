from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_cliens import get_public_users_client
from clients.users.users_schema import CreateUsersRequestSchema
from tools.assertions.authentification import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

from http import HTTPStatus


def test_login():
    public_users_client = get_public_users_client()

    request = CreateUsersRequestSchema()
    public_users_client.create_user(request=request)

    authentification_client = get_authentification_client()

    login_user_request = LoginRequestSchema(
        email=request.email,
        password=request.password
    )
    login_response = authentification_client.login_api(request=login_user_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(actual=login_response.status_code, expected=HTTPStatus.OK)
    assert_login_response(response=login_response_data)
    validate_json_schema(instance=login_response.json(), schema=login_response_data.model_json_schema())