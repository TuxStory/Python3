import json

with open('market.json') as f:
  data = json.load(f)

#print(data)

# Iterating through the json list
for i in data['markets']:
    print(i['name']," / ",i['id']," / ",i['lat']," / ",i['lng'])

# Closing file
f.close()
