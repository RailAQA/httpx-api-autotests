import json

data = {"test": "value", "name": "Игорь", "age": 20}

with open('test.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

