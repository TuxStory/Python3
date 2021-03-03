from bs4 import BeautifulSoup
import os, requests

result = []
url = "http://challenge01.root-me.org/programmation/ch1/"

#os.system("wget -O index.html "+url)
#test en python et non bash wget
headers = {
    'User-Agent': 'Firefox',
    'Content-Type': 'text/html',
}

response = requests.get(url, headers=headers)
html = response.text

#PAGE = open("index.html","r")
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('sub'):
    text = link.getText()
    result.append(text)

print (result[3])

URL = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="+result[3]
print (URL)
r = requests.get(url = URL)
print(r)
print(r.text)
print(r.status_code)
print(r.headers)
print(r.content)

# Je n'avais pas compris que je devais calculer :/

#You have only 2 seconds to send the result with the HTTP GET method
#(at http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=...)

#for link in soup.find_all('iframe'):
#    print(link.get('sub'))
