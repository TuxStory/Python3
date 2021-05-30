import json

with open('JsonParkTest.json') as f:
    data = json.load(f)

#print(data)
for i in data:
    print (i["ID"],i["Model"])
