import os

os.system("clear")

def imc(T,P): # IMC
    IMC = P/(T*T)
    return IMC

def imci(T,I): # IMC idéal 22
    BEST_POID = I * (T*T)
    return BEST_POID

def difpoid(poids,POIDS):
    DIFF = abs(poids - POIDS) #abs() valeur absolue
    return DIFF

Taille = input("Votre taille en mètre [ex 1.67]:")
Poid = input ("Votre poids en kilos [ex 72.4]:")
YOUR_IMC = imc(float(Taille),float(Poid))
print ("Votre imc est de :",round(YOUR_IMC,2))
YOUR_BEST_POID = imci(float(Taille),22)
print ("votre poid ideal devrait être de",round(YOUR_BEST_POID,2),"kg -> iMC = 22.")
## round(var,decimal) permet d'arrondir un résultat float
diff_poid = difpoid(float(Poid),float(YOUR_BEST_POID))
print ("Différence de ",round(diff_poid,2),"kg.")
