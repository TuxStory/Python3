#TEST
#Offre plein de fonctions pratiques qui permettent de faciliter le travail sur les
#séquences (liste, tuples, chaînes).
#Pour enchaîner plusieurs itérables (ça peut être des listes, des strings, ...) :

import itertools

#iterateur - count
Test1 = itertools.count(10)
print (Test1)

#cycle
Test2 = itertools.cycle('ABCD')
print (Test2)

#repeat
Test3 = itertools.repeat(10,5)
print (Test3)

#accumulate
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print (list(itertools.accumulate(data)))
#print (list(itertools.accumulate(data, operator.mul)))     # running product
print (list(itertools.accumulate(data, max)))              # running maximum

#permutation
print (list(itertools.permutations(['g', 'e', 'k'])))
antoine = (list(itertools.permutations(['a', 'n', 't', 'o', 'i', 'n', 'e'])))
cathia =  (list(itertools.permutations(['c', 'a', 't', 'h', 'i', 'a'])))

for element in cathia:
    print (element)
print (len(cathia))

for element in antoine:
    print (element)
print (len(antoine))

#combinaison
print ("==== chiffre ===")
y=[6,7,4,3]
print(list(itertools.permutations(y, 4)))
print ("Nb Combinaison :",len(list(itertools.permutations(y, 4))))

#chain
for x in itertools.chain([1, 2, 3], [4, 5], [6, 7]):
    print(x)

#Fonction product qui renvoie le produit cartésien :
print (">>> Product")
for x in itertools.product(['a', 'b', 'c'], ['A', 'B']):
    print(x)

#Fonction compress qui sélectionne seulement les éléments
#du premier itérable pour lesquels l'élément correspondant du 2ème itérable est vrai :
for x in itertools.compress(['A', 'B', 'C', 'D'], [1, 0, 1, 0]):
    print(x)
