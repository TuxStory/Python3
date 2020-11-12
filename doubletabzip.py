l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
#print('Result: {}'.format({a : b for a,b in zip(l1, l2)}))
#--------------------------
prenom = ["Root","Alfred","John","Mary","Hellen"]
nom = ["Wonderland","Stone","Spencer", "Flower","Doe"]
age = [24,33,87,8,41]
for p,n,a in zip(prenom,nom,age):
	print ("Bonjour, Je m'appelle {0} {1}. \nJ'ai {2} ans.\n".format(p,n,a))
