from pydantic import BaseModel, EmailStr
import pytest

from clients.authentification.authentification_client import AuthentificationClient, get_authentification_client
from clients.users.public_users_cliens import get_public_users_client, PublicUserClient
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUsersRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password

@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()

@pytest.fixture
def public_users_client() -> PublicUserClient:
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUserClient) -> UserFixture:
    request = CreateUsersRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request, response=response)