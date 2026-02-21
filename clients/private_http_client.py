from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema

from httpx import Client
from pydantic import BaseModel


class AuthentificationUserSchema(BaseModel):
    """
    Описание структуры запроса на авторизацию юзера
    """
    email: str
    password: str

def get_private_http_client(user: AuthentificationUserSchema) -> Client:
    """
    Функция создаёт приватный экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    authentification_client = get_authentification_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentification_client.login(login_request)
    

    return Client(
        timeout=30, 
        base_url="http://localhost:8000", 
        headers={"Authorization": f"Bearer {login_response.token.access_token}"})