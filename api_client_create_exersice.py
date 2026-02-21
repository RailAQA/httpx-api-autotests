from clients.courses.courses_client import get_private_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_private_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_client import AuthentificationUserSchema
from clients.users.public_users_cliens import get_public_users_client
from clients.users.users_schema import CreateUsersRequestSchema
from tools.fakers import fake


public_user_client = get_public_users_client()

create_user_request = CreateUsersRequestSchema()

create_user_response = public_user_client.create_user(request=create_user_request)
print(f"Create user data: {create_user_response}")

authenfication_user = AuthentificationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)

private_file_client = get_private_files_client(user=authenfication_user)

create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")

create_file_response = private_file_client.create_file(request=create_file_request)
print(f"Create user data: {create_file_response}")

private_user_client = get_private_courses_client(user=authenfication_user)

create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id,
)

create_course_response = private_user_client.create_course(
    request=create_course_request
)
print(f"Create course data: {create_course_response}")

private_exercise_client = get_private_exercise_client(user=authenfication_user)

create_exercise_request = CreateExerciseRequestSchema(
    course_id=create_course_response.course.id,)

response = private_exercise_client.create_exercice(request=create_exercise_request)
print(f"Create exercise data: {response}")
