import matplotlib.pyplot as plt
import numpy as np

w = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
 's', "t"]
n = [42, 50, 87, 25, 24, 22, 67, 43, 19, 18, 38, 18, 25, 17, 51, 15, 23, 45, 32, 13]

liste = list(zip(w,n)) 

print(liste.sorted())

plt.bar(range(len(w)),n)
plt.xticks(range(len(w)),w)

plt.show()