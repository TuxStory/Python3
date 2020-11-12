import matplotlib.pyplot as plt
import numpy as np

w = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
 's', "t"]
n = [42, 50, 87, 25, 24, 22, 67, 43, 19, 18, 38, 18, 25, 17, 51, 15, 23, 45, 32, 13]

liste = list(zip(w,n)) 
print(type(liste))
tri = sorted(liste, key=lambda liste: liste[1])
print(tri)
x, y = zip(*tri) 

plt.bar(range(len(x)),y)
plt.xticks(range(len(y)),x)
print(x, y)
plt.grid()
plt.title("Test tri")
plt.ylabel("Valeurs")
plt.xlabel("Lettres")
plt.show()