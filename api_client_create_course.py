from clients.courses.courses_client import CoursesClient, CreateCourseRequestDict, get_private_courses_client
from clients.files.files_client import CreateFileRequest, get_private_files_client
from clients.private_http_client import AuthentificationUserSchema
from clients.users.public_users_cliens import CreateUsersRequest, get_public_users_client
from tools.fakers import get_random_email


public_user_client = get_public_users_client()

create_user_request = CreateUsersRequest(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
    )

create_user_response = public_user_client.create_user(request=create_user_request)
print(f"Create user data: {create_user_response}")

authenfication_user = AuthentificationUserSchema(
    email=create_user_request["email"], 
    password=create_user_request["password"]
    )

private_file_client = get_private_files_client(user=authenfication_user)

create_file_request = CreateFileRequest(
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
    previewFileId=create_file_response["file"]["id"], 
    createdByUserId=create_user_response["user"]["id"]
    )

response = private_user_client.create_course(request=create_course_request)
print(f"Create user data: {response}")