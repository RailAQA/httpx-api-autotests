import httpx
from tools.fakers import fake

email = fake.email()
password = "pass"

payload = {
    "email": email,
    "password": password,
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

response = httpx.post(url="http://localhost:8000/api/v1/users", json=payload)

create_user_response_data = response.json()
print(f"Create user data: {create_user_response_data}")


payload_auth = {"email": email, "password": password}

response = httpx.post(
    url="http://localhost:8000/api/v1/authentication/login", json=payload_auth
)
login_user_response_data = response.json()
print(f"Create user data: {login_user_response_data}")


delete_user_headers = {
    "Authorization": f'Bearer {login_user_response_data["token"]["accessToken"]}'
}
response = httpx.delete(
    url=f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
    headers=delete_user_headers,
)
print(response.status_code)
