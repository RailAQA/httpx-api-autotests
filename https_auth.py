import httpx


def create_user():
    payload = {
  "email": "test@example.com",
  "password": "pass321",
  "lastName": "Puma",
  "firstName": "Amup",
  "middleName": "Yeah"
}
    response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

    print(f"Тело запроса: {response.json()}")

#create_user()

#{'user': {
# 'id': 'ba622d11-7986-455f-8463-988a3e4ea3a6',
#  'email': 'test@example.com',
#  'lastName': 'Puma',
#  'firstName': 'Amup',
#  'middleName': 'Yeah'}}

def login_view():
    payload = {
  "email": "test@example.com",
  "password": "pass321"
}
    response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=payload)
    print(response.status_code)
    print(response.json())
    return response

#login_view()

def refresh_token():
    refresh_token_payload = login_view().json()["token"]["refreshToken"]
    payload = {
  "refreshToken": refresh_token_payload
}
    
    response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", 
                         json=payload)
    
    for i in range(5):
        print('--')
    print(f"Response status code: {response.status_code}")
    print(f"Request body: {response.json()}")

refresh_token()