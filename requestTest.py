import requests, os

def main():
    os.system("clear")
    url = "https://fr-be.yahoo.com"
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    print("Texte :", r.text)
    print("Status :", r.status_code)
    print("Headers :", r.headers)
    print("Cookies :", r.cookies)
    
    with open("test.html", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

if __name__=="__main__":
    main()