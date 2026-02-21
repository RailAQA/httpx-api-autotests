from httpx import Response

from clients.api_client import APIClinet
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExercisesQuerySchema, UpdateExerciseRequestSchema
from clients.private_http_client import AuthentificationUserSchema, get_private_http_client


class ExercisesClient(APIClinet):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query.model_dump(by_alias=True))
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания по exercise_id.

        :param: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")
    
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url="/api/v1/exercises", 
            json=request.model_dump(by_alias=True)
            )
    
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            url=f"/api/v1/exercises/{exercise_id}", 
            json=request.model_dump(by_alias=True)
            )
    
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по exercise_id.

        :param: exercise_id - Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")
    
    def create_exercice(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

def get_private_exercise_client(user: AuthentificationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))