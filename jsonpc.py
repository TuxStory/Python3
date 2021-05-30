import json

with open('JsonParkTest.json') as f:
    data = json.load(f)

print(data)
