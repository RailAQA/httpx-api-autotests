from pydantic import BaseModel, EmailStr
import pytest

from clients.private_http_client import AuthentificationUserSchema
from clients.users.private_users_client import PrivateUserClient, get_private_users_client
from clients.users.public_users_cliens import get_public_users_client, PublicUserClient
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUsersRequestSchema
    response: CreateUserResponseSchema
    authentification_user: AuthentificationUserSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password
    
    @property
    def authentification_user(self) -> AuthentificationUserSchema:
        return AuthentificationUserSchema(email=self.email, password=self.password)

@pytest.fixture
def public_users_client() -> PublicUserClient:
    return get_public_users_client()

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUserClient:
    return get_private_users_client(function_user.authentification_user)

@pytest.fixture
def function_user(public_users_client: PublicUserClient) -> UserFixture:
    request = CreateUsersRequestSchema()
    response = public_users_client.create_user(request=request)
    return UserFixture(request=request, response=response)