import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

data = {
    "tittle": "Тест",
    "completed": False,
    "userId": "1"
}

response = httpx.post(url="https://jsonplaceholder.typicode.com/todos", json=data)

print("Статус код:", response.status_code)
print(response.json())

headers = {"authorization": "secret_key"}
response = httpx.get(url="https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.json())
print(response.request.headers)


params = {"userId": "1"}
response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response.url)
print(response.json())

file = {
    "file": ("example.txt", open("example.txt", "rb"))
    }
response = httpx.post(url="https://httpbin.org/post", files=file)

print(response.json())

with httpx.Client() as client:
    response_1 =client.get("https://jsonplaceholder.typicode.com/todos/1")
    response_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")


print(response_1.json(), response_2.json(), sep='\n')

client = httpx.Client(headers={"headers": "TEST"})
response1 = client.get("https://jsonplaceholder.typicode.com/todos/5")

print(response1.json())

try: 
    response = httpx.get("https://jsonplaceholder.typicode.com/tod")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print('Ошибка')

print(response.status_code)

try: 
    response = httpx.get("https://httpbin.org/delay/5", timeout=1)
except httpx.ReadTimeout as e:
    print(f'Ошибка {e}')