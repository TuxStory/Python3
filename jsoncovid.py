import json

Total = 0

with open('COVID19BE_MORT.json') as f:
  data = json.load(f)

#print(data)

# Iterating through the json list
for i in data:
#    print(i['DATE'],i['REGION'],i['AGEGROUP'],i['SEX'],i['DEATHS']) #DATA fichier non complete -> plantage
     print(i['DATE']," >>> ",i['DEATHS'])
     Total = i['DEATHS'] + Total

# Closing file
f.close()

print ("Total : ",Total)
