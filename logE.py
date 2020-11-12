import math

e = math.e
A = input("Entrez un nombre : ")
B = input("Entrez un nombre : ")

a = float(A)
b = float(B)

loga = math.log(a)
logb = math.log(b)
 
print("le logarithme népérien :", A,"= ", loga)
print("le logarithme népérien :", B,"= ", logb)

logc = loga+logb
A = int(A)
B = int(B)

print("Le Logarithme de A + B =",logc)
print(" A * B =", A * B)
print("E exposant",logc,"= ", e**logc)


