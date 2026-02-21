from clients.courses.courses_client import CreateCourseRequestDict, get_private_courses_client
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_private_exercise_client
from clients.files.files_client import get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_client import AuthentificationUserSchema
from clients.users.public_users_cliens import get_public_users_client
from clients.users.users_schema import CreateUsersRequestSchema
from tools.fakers import get_random_email


public_user_client = get_public_users_client()

create_user_request = CreateUsersRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
    )

create_user_response = public_user_client.create_user(request=create_user_request)
print(f"Create user data: {create_user_response}")

authenfication_user = AuthentificationUserSchema(
    email=create_user_request.email, 
    password=create_user_request.password
    )

private_file_client = get_private_files_client(user=authenfication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png", 
    directory="courses", 
    upload_file="./testdata/files/image.png")

create_file_response = private_file_client.create_file(request=create_file_request)
print(f"Create user data: {create_file_response}")

private_user_client = get_private_courses_client(user=authenfication_user)

create_course_request = CreateCourseRequestDict(
    title="string", 
    maxScore=20, 
    minScore=10, 
    description="string", 
    estimatedTime="30 минут", 
    previewFileId=create_file_response.file.id, 
    createdByUserId=create_user_response.user.id
    )

create_course_response = private_user_client.create_course(request=create_course_request)
print(f"Create course data: {create_course_response}")

private_exercise_client = get_private_exercise_client(user=authenfication_user)

create_exercise_request = CreateExerciseRequestDict(
    title="string", 
    courseId=create_course_response["course"]["id"], 
    maxScore=20, 
    minScore=2, 
    description="string", 
    estimatedTime="20"
    )

response = private_exercise_client.create_exercice(request=create_exercise_request)
print(f"Create exercise data: {response}")