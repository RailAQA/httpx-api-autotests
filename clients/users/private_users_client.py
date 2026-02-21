from clients.private_http_client import AuthentificationUserSchema, get_private_http_client
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema
from clients.api_client import APIClinet

from httpx import Response


class PrivateUserClient(APIClinet):
    """
    Клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            url=f"/api/v1/users/{user_id}", 
            json=request.model_dump(by_alias=True)
            )

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/users/{user_id}")
    
    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id=user_id)
        return GetUserResponseSchema.model_validate_json(response.text)
    
def get_private_users_client(user: AuthentificationUserSchema) -> PrivateUserClient:
    return PrivateUserClient(client=get_private_http_client(user=user))