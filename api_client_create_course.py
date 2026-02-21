from clients.courses.courses_client import get_private_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_client import AuthentificationUserSchema
from clients.users.public_users_cliens import get_public_users_client
from clients.users.users_schema import CreateUsersRequestSchema
from tools.fakers import fake


public_user_client = get_public_users_client()

create_user_request = CreateUsersRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

create_user_response = public_user_client.create_user(request=create_user_request)
print(f"Create user data: {create_user_response}")

authenfication_user = AuthentificationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)

private_file_client = get_private_files_client(user=authenfication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png", directory="courses", upload_file="./testdata/files/image.png"
)

create_file_response = private_file_client.create_file(request=create_file_request)
print(f"Create user data: {create_file_response}")

private_user_client = get_private_courses_client(user=authenfication_user)

create_course_request = CreateCourseRequestSchema(
    title="string",
    max_score=20,
    min_score=10,
    description="string",
    estimated_time="30 минут",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id,
)

response = private_user_client.create_course(request=create_course_request)
print(f"Create user data: {response}")
