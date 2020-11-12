#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Robots
import os
i=1

def player():
	joueur = input("Nom du joueur : ")
	print(" Type de Robot disponible ")
	print(" 1. Robot de classe RD")
	print(" 2. Robot de classe Goldo")
	print(" 3. Robot de classe  T800")
	type = input("Faites votre choix : ")
	return joueur,type

os.system("clear")
print ("************************************")
print ("* * * Welcome to Battle Robots * * *")
print ("************************************")
print()

joueur1,type1=player()
joueur2,type2=player()
#Création Robots

if type1 == "1":
	robot1 = Robots.RD(joueur1,100,True)
if type1 == "2":
	robot1 = Robots.GOLD(joueur1,100,True)
if type1 == "3":
	robot1 = Robots.T800(joueur1,100,True)

if type2 == "1":
	robot2 = Robots.RD(joueur2,100,True)
if type2 == "2":
	robot2 = Robots.GOLD(joueur2,100,True)
if type2 == "3":
	robot2 = Robots.T800(joueur2,100,True)

os.system("clear")

#Affichage
robot1.dessin()
print("======================================================================")
print("* Player 1 *") 
robot1.affiche()
print(robot1)
print("======================================================================")
print("* Player 2 *")
robot2.affiche()
print(robot2)

print("======================================================================")
print()
robot2.dessin()
input("Appyyez sur 'Enter' pour continuer...")

while (robot1.vie > 0) and (robot2.vie > 0):
	os.system("clear")
	print ( i, "===============================================")
	puissance1,arme1 = robot1.attaque()
	print (puissance1)
	#print (arme1)
	de1=robot1.defense()
	print ("=================================================")
	puissance2,arme2 = robot2.attaque()
	print (puissance2)
	#print (arme2)
	de2=robot2.defense()
	print ("=================================================")

	if de1 == 1:
		robot1.vie=robot1.vie-puissance2
	if de2 == 1:
		robot2.vie=robot2.vie-puissance1

	robot1.affiche()
	robot2.affiche()
	print("==================================================")
	print()
	if robot1.vie <= 0:
		robot1.statut = False
		robot1.vivant()
	if robot2.vie <= 0:
                robot2.statut = False
                robot2.vivant()
	input("Appyyez sur 'Enter' pour continuer...")
	i += 1

