import json
import urllib.request

#variable
Total = 0
UCI = 0

#Files
url = 'https://epistat.sciensano.be/Data/COVID19BE_MORT.json'
url2 = 'https://epistat.sciensano.be/Data/COVID19BE_HOSP.json'

#Downloading file
print('Beginning files download with urllib2...')
urllib.request.urlretrieve(url, 'COVID19BE_MORT.json')
urllib.request.urlretrieve(url2, 'COVID19BE_HOSP.json')

#Read file
with open('COVID19BE_MORT.json') as f:
    data = json.load(f)

with open('COVID19BE_HOSP.json') as f2:
    data2 = json.load(f2)

for i in data:
#     print(i['DATE']," >>> ",i['DEATHS'])
     Total = i['DEATHS'] + Total
f.close()

Date = data2[-1]['DATE'] #Valeur champ Date dans la dernière ligne

for i in data2:
    if i['DATE'] == Date:
        UCI = i['TOTAL_IN_ICU'] + UCI

print ("Sciensano Belgium")
print ("Date : ",Date)
print ("Total Décès : ",Total)
print ("Total Soin Intensif :",UCI)

#ancienne méthode pour la date 
#for i in data2:
#    Date = i['DATE']

