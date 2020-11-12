import os

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def analyse(phrase):
	print (bcolors.OKBLUE+"Analyse ..."+bcolors.ENDC)
	print ("La longeur totale est de :" , len(phrase))
	print ("Le nombre d'espaces est de :", len(phrase.split(" "))-1)
	print ("Le nombre de caractères est de :", len(phrase) - len(phrase.split(" "))+1)
	tab = (phrase.split( ))
	for i ,mots in enumerate(tab):
		print ("Le mot n°",i ,"est :",bcolors.FAIL+mots+bcolors.ENDC,"-->",len(mots),"lettres")
	print (bcolors.WARNING+"Inversé :"+bcolors.ENDC,phrase[::-1])
	print (bcolors.OKGREEN+"Upper :"+bcolors.ENDC,phrase.upper())
	print (bcolors.OKBLUE+"Lower :"+bcolors.ENDC,phrase.lower())

def main():
	os.system("clear")
	print ("TEXT".center(30,"="))
	Q = input(bcolors.BOLD+"Entrez une Phrase: "+bcolors.ENDC)
	analyse(Q)

if __name__=="__main__":
	main()
