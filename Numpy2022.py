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
print("Somme de F: ",np.sum(F))
print("Produit de F: ",np.prod(F))
print("Valeur Max (F): ", F.max())
print("Valeur Min (F): ", F.min())

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

E = np.sort(E)
print(E)

print("")
D = np.random.randint(10, size=40).reshape(5,8)
print(D)
print("Dimension : ",D.ndim)
print("Size : ",D.size)
print("Shape : ",D.shape)

print("")
F = np.array([1, 2, 3, 4, 5, 6])
G = np.array([3, 2, 6, 4, 1, 7])

list_of_coordinates= list(zip(F, G))
print(list_of_coordinates)
for element in list_of_coordinates:
    print (element)

K = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(K)
print(unique_values)
unique_values, indices_list = np.unique(K, return_index=True)
print(indices_list)
L = np.flip(K)
print(L)

#You can save it as “filename.npy” with:
#np.save('filename', a)

print("Attention")
M = [1,2,3,4]
N = [5,6,4,6]
O =  M + N
print("O:",O)

P = np.array([1,2,3,4])
Q = np.array([5,6,4,6])
R = P + Q
print('R:',R)
