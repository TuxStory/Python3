import os , re #, subprocess
from bs4 import BeautifulSoup #apt install python3-bs4
from pathlib import Path

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def choice():
	site = ["Twitter","Instagram","Debian : last amd64 .iso"]
	for i,c in enumerate(site):
		print (i,".",bcolors.OKGREEN+c+bcolors.ENDC)
	choix = input(bcolors.BOLD+"Entrez le n° de votre choix: "+bcolors.ENDC)
	return choix

def compte(C,Qurl):
	print (bcolors.OKBLUE+"Compte".center(50,"=")+bcolors.ENDC)
	user = Qurl
	twitter = "https://twitter.com/"
	instagram = "https://instagram.com/"
	debian = "https://www.debian.org/"
	if C =="0":
		url = twitter+Qurl
	if C =="1":
		url = instagram+Qurl
	if C =="2":
		url = debian
	return url

def SRC(URL):
	print (bcolors.OKBLUE+"Source".center(50,"=")+bcolors.ENDC)
	url = URL
	try:
		os.system("wget -O test.html "+url)
	except Exception as e:
		print ("Erreur ...")

def Analyse(C):
	print (bcolors.OKBLUE+"Analyse".center(50,"=")+bcolors.ENDC)
	Choix = C
	a = []
	PAGE = open("test.html","r")
	soup = BeautifulSoup(PAGE, 'html.parser')
	if Choix == "0":
		for link in soup.find_all('div'):
			test = link.get('data-image-url')
			if test != None:
				print (test)
				a.append(test)
	if Choix == "1":
		with open("test.html") as file:
			for line in file:
				#urls = re.findall(r'display_url+\"+:\"https:\/\/[a-zA-Z0-9-_\.\/\?=&]+jpg', line) MISE A JOUR 20 Dec 2018
				urls = re.findall(r'display_url+\"+:\"https:\/\/[a-zA-Z0-9-_\.\/\?=&]+jpg\?+[a-zA-Z0-9-_\.\/\?=&]+net',line)
				for img in range (0,len(urls)):
					a.append((urls[img].replace('display_url":"',' ')))
					print(a[img])
	if Choix =="2":
		with open("test.html") as file:
			for line in file:
				urls = re.findall(r'https?://[a-zA-Z0-9-_\.\/\?=&]+iso', line)
				if (urls) != []:
					a.append(urls[0])
					print (urls)
	return a

def DL(TAB,choix):
	CHOIX = choix
	print (bcolors.OKBLUE+"Téléchargement".center(50,"=")+bcolors.ENDC)
	for image in range(0,len(TAB)):
		print (bcolors.WARNING,"Téléchargement de : ",bcolors.ENDC,TAB[image])
		if choix == "0":
			os.system("wget "+TAB[image]+":large")
		else:
			os.system("wget "+TAB[image])


def DLDIR(Name):
	os.system("mkdir "+Name)
	#subprocess.call("mkdir "+Name,shell=True)
	home = str(Path.home())
	os.chdir(home+"/Bureau/"+Name)

def main():
	tab = []
	home = str(Path.home())
	os.system("clear")
	print (bcolors.OKBLUE+"Multi Choice Dump".center(50,"=")+bcolors.ENDC)
	C = choice()
	Qurl = input(bcolors.BOLD+"Entrez un compte: "+bcolors.ENDC)
	URL = compte(C,Qurl)
	print("Télécharmenent du code HTML... :",bcolors.FAIL+URL+bcolors.ENDC)
	SRC(URL)
	tab = Analyse(C)
	DLDIR(Qurl)
	DL(tab,C)
	os.chdir(home+"/Bureau")
	os.system("rm test.html")

if __name__=="__main__":
	main()
