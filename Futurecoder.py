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
