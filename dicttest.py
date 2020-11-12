import subprocess

subprocess.call("clear")

Utilisateur = {
    "Nom": "Courantdair",
    "Prenom": "Basile",
    "Profession": "Danseur",
    "Age": 52,
    "DateNaissance": "02/06/1966",
    "Ville": "Marseille",
    "Taille": 1.75,
    "Telephone": "0581657415"
}

Utilisateur2 = {
    "Nom": "Atkinson",
    "Prenom": "Rowan",
    "Profession": "Acteur",
    "Age": 63,
    "DateNaissance": "06/01/1955",
    "Ville": "Consett",
    "Taille": 1.81,
     "Telephone": "045621784"
}

def Print_Tab(Tab):
    for user in Tab:
        for k, v in user.items():
            print(k,":",v)
        print(" ")

print(Utilisateur)
print("TEST 1".center(50,"-"))
print(Utilisateur["Age"])
print("TEST 2".center(50,"-"))
Permis = input("Cette personne a t'elle le permis de conduire ? (Oui/Non) :")
Utilisateur["Permis"]=Permis
print(Utilisateur)
print("TEST 3".center(50,"-"))
for k, v in Utilisateur.items():
    print(k,":", v)
#Il existe aussi les option Utilisateur.keys() ou Utilisateur.values()
#>>> fruits = {"pommes":21, "melons":3, "poires":31}
#>>> for valeur in fruits.values():
#...     print(valeur)

print("TEST 4".center(50,"-"))
Tab = []
Tab.append(Utilisateur)
Tab.append(Utilisateur2)
print(Tab)
print("Resultat".center(50,"-"))
Print_Tab(Tab)

print("TEST 5".center(50,"-"))
print (Tab[1]["Age"])

print("TEST 6".center(50,"-"))
Name = input("Entrer un nom de famille:")
FirstName = input("Entrer un prénom:")
Pro = input("Entrer une profession:")
Age = int(input("Entrer un age:"))
DateN = input("Entrer une date:")
Ville = input("Entrer une ville:")
Taille = float(input("Entrer une Taille:"))
Telephone = input("Entrer un numéro de téléphone:")
Permis = input("Cette personne a t'elle le permis de conduire ? (Oui/Non) :")
Utilisateur3 = {"Nom":Name,"Prenom":FirstName,"Age":Age,"DateNaissance":DateN,"Ville":Ville,"Taille":Taille,"Telephone":Telephone,"Permis":Permis}
Tab.append(Utilisateur3)
print("Resultat".center(50,"-"))
Print_Tab(Tab)
