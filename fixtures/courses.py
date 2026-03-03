from pydantic import BaseModel
import pytest

from clients.courses.courses_client import get_private_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.authentification import UserFixture
from fixtures.files import FileFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_private_courses_client(function_user.authentification_user)

@pytest.fixture
def function_course(
    courses_client: CoursesClient, 
    function_file: FileFixture, 
    function_user: UserFixture
    ) -> CourseFixture:
    request = CreateCourseRequestSchema()
    response = courses_client.create_course(request=request)
    return CourseFixture(request=request, response=response)