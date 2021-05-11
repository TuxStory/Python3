import itertools as it

x=[1,2,4,5,8,9]
y=[6,7,4,3]

def fonction(Tab):
    for i, combi in enumerate(Tab):
        print (i,">>>", combi)
    print ("Nombre : ",len(Tab))

#Permutations
#print(list(it.permutations(x, 4)))
Combi = list(it.permutations(x, 4))
Combi2 = list(it.permutations(y, 4))

#Affichage
Result1=fonction(Combi)
print("="*30)
Result2=fonction(Combi2)
