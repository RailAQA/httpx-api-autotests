from clients.private_http_client import AuthentificationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_cliens import get_public_users_client
from clients.users.users_schema import CreateUsersRequestSchema
from tools.fakers import fake


public_user_client = get_public_users_client()

create_user_request = CreateUsersRequestSchema(
    email=fake.email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)
create_user_response_response = public_user_client.create_user(
    request=create_user_request
)

print(f"Create user data: {create_user_response_response}")

user = AuthentificationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)
private_user_client = get_private_users_client(user=user)

get_user_response = private_user_client.get_user(create_user_response_response.user.id)
print(f"Get user data: {get_user_response}")
