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

print("------Ex2------")

ligne = '+' + nom + '+'
espaces = ''
for _ in nom:
    espaces += ' '

print(ligne)
for caractere in nom:
    print(caractere + espaces + caractere)
print(ligne)

print("------Ex3------")
nom = 'World'
espace =''
for caractere in nom:
    print(espace+caractere)
    espace+=" "
print("------Ex4------")
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
print("------Ex5------")
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

print("------Ex6------")
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

print("------Ex7------")
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