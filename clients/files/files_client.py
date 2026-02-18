from httpx import Response

from clients.api_client import APIClinet
from typing import TypedDict

from clients.private_http_client import AuthentificationUserDict, get_private_http_client


class CreateFileRequest(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class File(TypedDict):
    """
    Описание структуры файла
    """
    id : str
    filename : str
    directory : str
    url : str

class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа на создание файла
    """
    file: File

class FileClient(APIClinet):
    """
    Клиент для работы с /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequest) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url="/api/v1/files", 
            data=request, 
            files={"upload_file": open(request["upload_file"], "rb")})
    
    def create_file(self, request: CreateFileRequest) -> CreateFileResponseDict:
        response = self.create_file_api(request=request)
        return response.json()
    
def get_private_files_client(user: AuthentificationUserDict) -> FileClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FileClient(client=get_private_http_client(user=user))