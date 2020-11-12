import math

A = input("Entrez un nombre : ")
B = input("Entrez un nombre : ")

a = float(A)
b = float(B)

loga = math.log10(a)
logb = math.log10(b)
 
print("le logarithme en base 10 de :", A,"= ", loga)
print("le logarithme en base 10 de :", B,"= ", logb)

logc = loga+logb
A = int(A)
B = int(B)

print("Le Logarithme de A + B =",logc)
print(" A * B =", A * B)
print("10 exposant",logc,"= ", 10**logc)


