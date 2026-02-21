from httpx import Response

from clients.api_client import APIClinet
from typing import TypedDict

from clients.private_http_client import AuthentificationUserSchema, get_private_http_client
from clients.users.public_users_cliens import User


class UpdateUserRequest(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class GetUserResponseDict(TypedDict):
    user: User

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

    def update_user_api(self, user_id: str, request: UpdateUserRequest) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/users/{user_id}")
    
    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id=user_id)
        return response.json()
    
def get_private_users_client(user: AuthentificationUserSchema) -> PrivateUserClient:
    return PrivateUserClient(client=get_private_http_client(user=user))