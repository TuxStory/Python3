#!/usr/bin/pyhton3.5
#-*- coding: utf-8 -*-

import humanity

#humain1=humanity.human("Antoine","Even","Homme","40")
#humain1.affiche()
#humain1.vie = True
#humain1.vivant()
fille = 0 ; garcon = 0

homme = list()
for i in range(10):
	homme.append(humanity.human("Bob",(i),"Homme","20","Belgique"))
	homme[i].affiche()
	homme[i].vivant()
	homme[i].patrie()

femme = list()
for j in range(10):
	femme.append(humanity.human("Eva",(j),"Femme","20","Belgique"))
	femme[j].affiche()
#	femme[j].vivant()
#	femme[j].patrie()

print ("--------------------------------------------")

def reproduction():
	global i,j
	global fille,garcon
	for x in range(10):
		geneh = homme[x].chromo()
#		print ("Je donne un chromosome :", geneh)
		genef =  femme[x].chromo()
#		print ("Je donne un chromosome :", genef)
		geneb = geneh + genef
		print ("Résultat :", geneb)
		if geneb == "xx":
			j += 1; fille += 1
			femme.append(humanity.human("Charlotte",(j),"Femme","1","Belgique"))
			femme[j].affiche()
		if geneb == "yx":
			i += 1; garcon += 1
			homme.append(humanity.human("Alfred",(i),"Homme","1","Belgique"))
			homme[i].affiche()

	print ("---------------------------------------------")
	print ("Nombre de filles", fille)
	print ("Nombre de garçons", garcon)

reproduction()
reproduction()
