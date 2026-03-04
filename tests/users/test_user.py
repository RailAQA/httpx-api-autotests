from clients.users.public_users_cliens import PublicUserClient
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

from http import HTTPStatus
import pytest

from tools.assertions.users import assert_create_user_response


@pytest.mark.user
class TestUser:
        @pytest.mark.parametrize(
                "email", 
        [
                fake.email(domain="mail.ru"), 
                fake.email(domain="gmail.com"), 
                fake.email(domain="example.com")
        ]
        )
        def test_create_user(self, email: str, public_users_client: PublicUserClient):
                request = CreateUsersRequestSchema(email=email)
                response = public_users_client.create_user_api(request=request)
                response_data = CreateUserResponseSchema.model_validate_json(response.text)

                assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
                assert_create_user_response(request=request, response=response_data)

                validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

