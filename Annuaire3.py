import subprocess
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ajout():

    Name = input("Entrer un nom de famille :")
    FirstName = input("Entrer un prénom :")
    Pro = input("Entrer une profession :")
    Age = input("Entrer un age :")
    DateN = input("Entrer une date :")
    Ville = input("Entrer une ville :")
    Taille = input("Entrer une Taille :")
    Telephone = input("Entrer un numéro de téléphone:")
    Permis = input("Cette personne a t'elle le permis de conduire ? (Oui/Non) :")
    Email = input("Entrer une adresse E-mail :")
    NewEntry = {"Nom":Name,"Prenom":FirstName,"Profession":Pro,"Age":Age,"DateNaissance":DateN,"Ville":Ville,"Taille":Taille,"Telephone":Telephone,"Permis":Permis,"Email":Email}
    return NewEntry

def Print_Tab(Tab):
    for user in Tab:
        for k, v in user.items():
            print(k,":",v)
        print(" ")

def recherche(Nom,Annuaire):
    compteur = 0
    for i in range(len(Annuaire)):
        for valeur in Annuaire[i].values():
            if Nom == valeur:
                print(" ")
                print(bcolors.OKGREEN,"[ OK ]",bcolors.ENDC," Ocuurance trouvée ! : ",valeur)
                print(" ")
                print(bcolors.WARNING,"Utilisateur : ",i,bcolors.ENDC)
                compteur = compteur + 1
                for k, v in Annuaire[i].items():
                    print(k," : ", v)
    print(" ")
    print("Total des occurances trouvées : ",bcolors.OKGREEN,compteur,bcolors.ENDC)

def effacer(Annuaire):
    for i in range(len(Annuaire)):
        print ("N°",bcolors.FAIL,i,bcolors.ENDC,Annuaire[i]["Nom"],Annuaire[i]["Prenom"])
    try:
        deleteitem = int(input("Quel entrée voulez-vous effacer ? :"))
        print ("N°",bcolors.OKBLUE,deleteitem,bcolors.ENDC,Annuaire[deleteitem]["Nom"],Annuaire[deleteitem]["Prenom"])
        conf = input("Voulez-vous effacer cette entrée ? (Oui/Non) :")
        if conf == "Oui" or "oui" or "OUI" or "O" or "o":
            print (bcolors.OKGREEN,"[ OK ]",bcolors.ENDC," Entrée n°",deleteitem,"effacée !")
            del Annuaire[deleteitem]
        else:
            print (bcolors.FAIL+"[ Erreur ]"+bcolors.ENDC+" Aucun utilisateur effacé ! ")
    except TypeError:
        print(bcolors.FAIL,"[ Erreur ]",bcolors.ENDC," Une erreur est survenue !")
        return
    except ValueError:
        print(bcolors.FAIL,"[ Erreur ]",bcolors.ENDC," Entrer une valeur valide !")
    except IndexError:
        print(bcolors.FAIL,"[ Erreur ]",bcolors.ENDC," Entrer une valeur valide !")

def ecriture(TAB):
    try:
        with open("data_file.json", "w") as write_file:
            json.dump(TAB,write_file,indent=4)
        print ("Sauvegarde de l'annuaire",bcolors.OKGREEN,"[ OK ]",bcolors.ENDC)
    except:
        print("Sauvegarde non effectuée !",bcolors.FAIL,"[ Erreur ]",bcolors.ENDC)

def lecture():
    try:
        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
            print("Annuaire importé !",bcolors.OKGREEN,"[ OK ]",bcolors.ENDC)
            return data
    except:
        print("[ Erreur ] L'annuaire n'a pas été trouvé !")

def main():

    subprocess.call("clear")
    quit = False
    Annuaire = lecture()
    while quit != True:
        print(bcolors.OKBLUE+"Menu".center(50,"-")+bcolors.ENDC)
        print("1. Affichage de l'annuaire.")
        print("2. Recherche d'un contact")
        print("3. Ajouter un contact.")
        print("4. Effacer un contact.")
        print("5. Sortie")
        print(bcolors.OKBLUE+"-"*50+bcolors.ENDC)
        action = input("Que voulez-vous faire : ")

        if action == "1":
            subprocess.call("clear")
            print(bcolors.OKBLUE+"Annuaire Python 3".center(50,"-")+bcolors.ENDC)
            Print_Tab(Annuaire)
        if action == "2":
            subprocess.call("clear")
            Recherche = input("Qui cherchez-vous ? : ")
            recherche(Recherche,Annuaire)
        if action == "3":
            subprocess.call("clear")
            print("Annuaire Python 3".center(50,"-"))
            NewUser = ajout()
            Annuaire.append(NewUser)
        if action == "4":
            effacer(Annuaire)
        if action == "5":
            ecriture(Annuaire)
            quit = True

if __name__=="__main__":
	main()
