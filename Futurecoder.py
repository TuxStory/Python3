#!/usr/bin/python3

# Exercice de FutureCoder
# https://futurecoder.io/

nom = 'World'
car = ''

for caractere in nom:
    car += '-' 
print("+"+car+"+")
print ("|"+nom+"|")
print("+"+car+"+")

print("------EX2------")

ligne = '+' + nom + '+'
espaces = ''
for _ in nom:
    espaces += ' '

print(ligne)
for caractere in nom:
    print(caractere + espaces + caractere)
print(ligne)

print("------EX3------")
nom = 'World'
espace =''
for caractere in nom:
    print(espace+caractere)
    espace+=" "
print("------EX4------")
phrase = 'Hello World'
phrase2 = ''
First = True

for caractere in phrase:
    if First:
        caractere = caractere.upper()
        phrase2 += caractere
        First = False
    else:
        caractere = caractere.lower()
        phrase2 += caractere

print(phrase2)
print("------EX5------")
phrase = 'Hello World'
phrase2 = ''
Upper = True

for caractere in phrase:
    if Upper:
        caractere = caractere.upper()
        phrase2 += caractere
        Upper = False
    else:
        caractere = caractere.lower()
        phrase2 += caractere
        Upper = True

print(phrase2)

print("------EX6------")
nom = 'Melissa'
nouveau_nom = ''
for c in nom:
    if c == 's':
        c = '$'
    if c == "e":
        c = '3'
    if c == 'a':
        c = '@'
    nouveau_nom += c

print(nouveau_nom)

print("------EX7------")
adn = 'AGTAGCGTC'
adn_inverse = ''
for caractere in adn:
    if caractere == 'A':
        caractere = 'T'
    elif caractere == 'T':
            caractere = 'A'
    elif caractere == 'G':
        caractere = 'C'
    elif caractere == 'C':
            caractere = 'G'
    adn_inverse += caractere

print(adn_inverse)

print("------EX8------")
x_1 = 30
x_2 = 10
x_3 = 22

if x_1 < x_2:
    if x_1 < x_3:
        premier = x_1
    else:
        premier = x_3
else:
    if x_2 < x_3:
        premier = x_2
    else:
        premier = x_3
print(premier)

#Solution Elegante
premier = x_1

if x_2 < premier:
    premier = x_2

if x_3 < premier:
    premier = x_3

print(premier)

print('------EX9------')

mots = ['Ceci', 'est', 'une', 'liste']
separateur = ' - '

total = ''
for mot in mots:
    if mot != mots[0]:
        total += separateur + mot 
    else:
        total += mot

print(total)
#solution du cours :
mots = ['Ceci', 'est', 'une', 'liste']
separateur = ' - '
total = ''
pas_premier = False

for mot in mots:
    if pas_premier:
        total += separateur
    total += mot
    pas_premier = True

print(total)
print("------EX10------")
nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5]
i = 0
for nombre in nombres:
    nombres[i] = nombre * 2
    i+=1
print(nombres)

print("------Ex11------")
nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5]
Tab = []
for nombre in nombres:
    if nombre > 5:
        Tab.append(nombre)
print(Tab)

print("------EX12------")
choses = ['Ceci', 'est', 'une', 'liste']
cible = 'est'
Var = False

for mot in choses:
    if mot == cible:
        Var = True
        break

print(Var)

print("------EX13------")
choses = ['sur', 'le', 'chemin', 'vers', 'le', 'magasin']
cible = 'le'

i = 0
for mot in choses:
    if mot == cible:
        print (i)
        break
    i += 1

print("------EX14------")
chaine_1 = 'Hello'
chaine_2 = 'World'

for i in range(len(chaine_1)):
    car1 = chaine_1[i]
    car2 = chaine_2[i]
    print(car1+ ' ' +car2)

print("------EX15------")
chaine_1 = 'Goodbye'
chaine_2 = 'World'

longueur_1 = len(chaine_1)
longueur_2 = len(chaine_2)

if longueur_1 > longueur_2:
    long = longueur_1
else:
    long = longueur_2

for i in range(long):
    if i < len(chaine_1):
        car1 = chaine_1[i]
    else:
        car1 = " "
    
    if i < len(chaine_2):
        car2 = chaine_2[i]
    else:
        car2 = " "

    print(car1+ ' ' +car2)

print("------EX16------")
chaine_1 = 'Hello'
chaine_2 = 'Élisabeth'

longueur_1 = len(chaine_1)
longueur_2 = len(chaine_2)

if longueur_1 > longueur_2:
    long = longueur_1
else:
    long = longueur_2

for i in range(long):
    if i < len(chaine_1):
        car1 = chaine_1[i]
    else:
        car1 = " "
    
    if i < len(chaine_2):
        car2 = chaine_2[i]
    else:
        car2 = " "

    print(car1+ ' ' +car2)

print("------EX17------") 
x = ['a', 'b', 'c']
x.append(x.pop(0))
print(x)

print("------EX18------")
x = ['a', 'b', 'c']
x[len(x) - 1] = x[0]
print(x)

print("-----EX19-----")
x = ['a', 'b', 'c']
y = x + [x[0]]
print(y)

print('------EX20------')
x = [1, 2, 0, 3]
x.pop(x.index(0))
print(x)

print('------EX21------')
print(max([21, 55, 4, 91, 62, 49]))

print('------EX22------')
nombres = [1, 2, 3, 4, 5]
nombres.insert(2,9)
print(nombres)

print("------EX23------")
for chiffre in range(1,13):
    for nombre in range(1,13):
        print(f'{chiffre} x {nombre} = {chiffre*nombre}')
    print('---')

print("------EX24------")
joueurs = ["Alice","Bob","Carole"]
for prenom in joueurs:
    for prenom2 in joueurs:
        if prenom != prenom2:
            print(f'{prenom} contre {prenom2}')


print("------EX25------")
lettres = "ABCD"
for lettre in lettres:
    for lettre2 in lettres:
        for lettre3 in lettres:
            for lettre4 in lettres:
                print(f'{lettre}{lettre2}{lettre3}{lettre4}')

print("------EX26------")
taille = 5
longeur = taille
for i in range(taille):
    print("+"*taille)
    taille = taille -1

taille = 5
longueur = taille

#Deuxième solutiuon attendue 
for i in range(taille):
    for j in range(longueur):
        print("+",end='')
    print()
    longueur = longueur - 1

print("------EX27------")
mot = 'Fabuleux'
voyelles = []
consonnes = []
for lettre in mot:
    if lettre.lower() in 'aeiouy':
        voyelles.append(lettre)
    else:
        consonnes.append(lettre)
print(voyelles)
print(consonnes)

print("------EX28------")