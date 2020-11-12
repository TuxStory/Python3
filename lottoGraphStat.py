import matplotlib.pyplot as plt
import numpy as np
import random

nb = 100

def Lotto():
    lotto = range(1,47)
    tirage = random.sample(lotto,7)
    return tirage

def Matrice():
    matrice = []
    for i in range(nb):
        L = Lotto()
        matrice.append(L)
    return matrice

Stat = Matrice()
#print(Stat)
unique, counts = np.unique(Stat, return_counts=True)
c = list(zip(unique, counts))
print(c)
tri = sorted(c, key=lambda c: c[1])
print("TRI".center(20,"*"))
print(tri)
x, y = zip(*tri)

#y_pos = np.arange(len(counts))
plt.subplot(211)
plt.title("Lotto Stats by Counts")
bar = plt.bar(range(len(x)), y, align='center', alpha=0.5)
plt.xticks(range(len(y)),x)
plt.grid()
plt.subplot(212)
bar = plt.bar(range(len(unique)), counts, align='center', alpha=0.5,color='g')
plt.xticks(range(len(counts)),unique)
plt.title("Lotto Stats by Number")
plt.grid()
#plt.legend(str(nb))

plt.show()