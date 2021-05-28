import os, glob, sys

def ecrire(liste):
    fichier = "liste.txt"
    print("Ecriture dans le fichier '{}'...".format(fichier))
    with open(fichier, 'w') as f:
        for item in liste:
            f.write(item)
            f.write("\n")
    print("OK!")

def main():
    if len(sys.argv) != 2:
        print("Usage : listwriter2 /dossier")
        sys.exit()
    else:
        ext = input("Type d'extention : ")
        chemin = str(sys.argv[1])+"**/*"
        print(chemin)
        liste = glob.glob(chemin+ext,recursive=True)
        ecrire(liste)    

if __name__=="__main__":
    main()
