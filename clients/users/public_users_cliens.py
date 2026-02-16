from clients.api_client import APIClinet

from httpx import Response
from typing import TypedDict

from clients.public_http_builder import get_public_http_client

class CreateUsersRequest(TypedDict):
  """
    Описание структуры запроса на создание пользователя.
    """
  email: str
  password: str
  lastName: str
  firstName: str
  middleName: str

class User(TypedDict):
  id: str
  email: str
  lastName: str
  firstName: str
  middleName: str

class CreateUserResponseDict(TypedDict):
   user: User

class PublicUserClient(APIClinet):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUsersRequest) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с email, password, lastname, firstname, middlename.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
    
    def create_user(self, request: CreateUsersRequest) -> CreateUserResponseDict:
       response = self.create_user_api(request=request)
       return response.json()
    
def get_public_users_client() -> PublicUserClient:
   return PublicUserClient(client=get_public_http_client())
