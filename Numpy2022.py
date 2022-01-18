import numpy as np

A = np.arange(10)
print(A)

B = np.random.rand(20)
B = np.reshape(B, (2,10))
print(B)

C = np.random.randint(10, size=30).reshape(3,10)
print(C)

d = np.ones(5)
D = np.diag(d,2)
print(D)
dd = np.ones((2,10))
print(dd)
print(B<dd)

print("Comparaison")
E=(B*2)
print("E :",E)
print(E<dd)

print("")
F = np.array([2,5,6,0,5,4,6,8,9,5,3,6])
G = np.array([6,5,4,1,2,3,6,8,7,4,5,2])
print(F<G)
print(F==G)
print("Indice élément max :",np.argmax(F))
print("Valeur :",F[np.argmax(F)])
print("Indice élément min :",np.argmin(F))
print("Valeur :",F[np.argmin(F)])
print(np.sum(F))
print(np.prod(F))