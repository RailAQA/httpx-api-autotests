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


print(response.status_code)
print(response.json())
create_user_response_data = response.json()

payload_auth = {"email": email, "password": password}

response = httpx.post(
    url="http://localhost:8000/api/v1/authentication/login", json=payload_auth
)
print(response.json())
login_user_response_data = response.json()

headers = {
    "Authorization": f'Bearer {login_user_response_data["token"]["accessToken"]}'
}
response = httpx.get(
    url=f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
    headers=headers,
)
print(response.json())
print(response.status_code)
