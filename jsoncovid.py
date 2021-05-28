import json
import urllib.request

Total = 0

#Downloading file
print('Beginning file download with urllib2...')
url = 'https://epistat.sciensano.be/Data/COVID19BE_MORT.json'
urllib.request.urlretrieve(url, 'COVID19BE_MORT.json')

#Read file
with open('COVID19BE_MORT.json') as f:
  data = json.load(f)

# Iterating through the json list
for i in data:
#    print(i['DATE'],i['REGION'],i['AGEGROUP'],i['SEX'],i['DEATHS']) #DATA fichier non complete -> plantage
     print(i['DATE']," >>> ",i['DEATHS'])
     Total = i['DEATHS'] + Total

# Closing file
f.close()

print ("Total : ",Total)
