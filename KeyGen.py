#/bin/python3
import random
import os
#Test Pour Raspberry Pi
os.system("clear")

print('''
==== Générateur de mot de passe ====
''')

caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRST*$?!%@|&€$'
nommbre = int(input("Nombre de mot de passe ? :"))
longeur = int(input("Longueur du mot de passe ? :"))

print("Voici les mots de passe : ")

for mdp in range(nommbre):
    motdepasse = ""
    for c in range(longeur):
            motdepasse += random.choice(caracteres)
    print(motdepasse)