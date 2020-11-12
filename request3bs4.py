import requests, os, bs4, re
import tqdm as tqdm

def main():
    os.system("clear")
    print("HTML".center(25,"-"))
    url = input("Entrez une adresse html :")
    bar = tqdm.trange(1)
    bar.set_description("Code Source")
    
    for i in bar:
        headers = {'user-agent': 'Firefox'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        Soup = bs4.BeautifulSoup(r.text, "html.parser")
        elems = []
        for link in Soup.find_all('a',href= True):
            #print (link.get('href'))
            elems.append(link.get('href'))
     
    bar2 = tqdm.trange(len(elems))
    bar2.set_description("Analyse ...")
    search = ".iso"
    result = []
    for j in bar2:
        if search in elems[j]:
            result.append(elems[j])
    for k in range(len(result)):
        print(result[k])
        
    bar3 = tqdm.trange(len(result))
    bar3.set_description("Download ..")
    for l in bar3:
        name = result[l].split("/")[-1] 
        with open("%s" % name,"wb") as file:
            #open('{0}.csv'.format(name), 'wb')
            down = requests.get(result[l])
            down.raise_for_status()      
            file.write(down.content)
               
if __name__=="__main__":
    main()