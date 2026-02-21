from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserResponseSchema, CreateUsersRequestSchema
from clients.api_client import APIClinet


from httpx import Response


class PublicUserClient(APIClinet):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUsersRequestSchema) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с email, password, lastname, firstname, middlename.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))
    
    def create_user(self, request: CreateUsersRequestSchema) -> CreateUserResponseSchema:
       response = self.create_user_api(request=request)
       return CreateUserResponseSchema.model_validate_json(response.text)
    
def get_public_users_client() -> PublicUserClient:
   return PublicUserClient(client=get_public_http_client())
