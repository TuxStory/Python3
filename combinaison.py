import itertools as it

x=[1,2,4,5,8,9]
y=[6,7,4,3]
#print(list(it.permutations(x, 4)))
Combi = list(it.permutations(x, 4))
Combi2 = list(it.permutations(y, 4))

for i, combi in enumerate(Combi):
    print (i,">>>", combi)

print ("Nombre : ",len(Combi))
