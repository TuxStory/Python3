import requests, os
import tqdm as tqdm

def main():
    os.system("clear")
    print("HTML".center(25,"-"))
    bar = tqdm.trange(1)
    for i in bar:
        bar.set_description("Code Source")
        url = "https://fr-be.yahoo.com"
        headers = {'user-agent': 'Firefox'}
        r = requests.get(url, headers=headers)
        
        with open("source.html", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

if __name__=="__main__":
    main()