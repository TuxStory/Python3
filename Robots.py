#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Robot:
	def __init__(self,nom,vie,statut):
		self.nom = nom
		self.vie = vie
		self.statut = True

	def affiche(self):
		print ("Nom :",self.nom, " | Point de vie :", self.vie)

	def vivant(self):
		if self.statut == True:
			print ("Je suis en vie.",end=" ")
		if self.statut == False:
			print (self.nom + " : Je ne fonctionne plus adéquatement !!!")
			print ("Vous m'avez vaincu ! Bravo !")

	def attaque(self):
		print ("Attaque : " + self.nom,end=" ")
		import random
		puissance = random.randint(0,20)
		arme = random.choice(['1','2'])
		if arme == "1":
			print (self.weapons, "Puissance ",end=" ")
		else:
			print (self.weapons2, "Puissance ",end=" ")
			puissance=puissance+10
		return puissance,arme

	def defense(self):
		print ("Defense : " + self.nom,end=" ")
		import random
		d = random.randint(0,100)
		qi = int(self.qi)
		res = int(self.resistance)
		if (qi + res + d)/2 > 100:
			print ("J'ai évité l'attaque")
		else:
			print("** Je suis trouché !! **")
			return 1

class RD(Robot):
	def __init__(self,nom,vie,statut):
		Robot.__init__(self,nom,vie,statut)
		self.taille = "1"
		self.poids = "32"
		self.gender = "Male"
		self.weapons = "Pique électrique"
		self.weapons2 = "Scie circulaire"
		self.qi = "100"
		self.resistance = "65"

	def __str__(self):
		return "Taille  : " + self.taille + " Mètre | Poids : " + self.poids + " Kg | QI : " + self.qi + " | Résistance : " + self.resistance

	def dessin(self):
		print("   .=. ")
		print("  '==c|")
		print("  [)-+|")
		print("  //'_|")
		print(" /]==;\ ")

class GOLD(Robot):
	def __init__(self,nom,vie,statut):
		Robot.__init__(self,nom,vie,statut)
		self.taille = "30"
		self.poids = "150"
		self.gender = "Male"
		self.weapons = "Laser"
		self.weapons2 = "Missile"
		self.qi = "50"
		self.resistance = "100"
		self.fly = True


	def __str__(self):
		return "Taille  : " + self.taille + " Mètres | Poids : " + self.poids + " Tonnes | QI : " + self.qi + " | Résistance : " + self.resistance

	def dessin(self):
		print("      ___       ___ ")
		print("     [___] /~\ [___]")
		print("     |ooo|.\_/.|ooo|")
		print("     |888||   ||888|")
		print("    /|888||   ||888|\ ")
		print("  /_,|###||___||###|._\ ")
		print(" /~\  ~~~ /[_]\ ~~~  /~\ ")
		print("(O_O) /~~[_____]~~\ (O_O) ")
		print("     (  |       |  ) ")
		print("    [~` ]       [ '~] ")
		print("    |~~|         |~~| ")
		print("    |  |         |  | ")
		print("   _<\/>_       _<\/>_")
		print("  /_====_\     /_====_\ ")

class T800(Robot):
	def __init__(self,nom,vie,statut):
		Robot.__init__(self,nom,vie,statut)
		self.taille = "1.90,"
		self.poids = "130"
		self.gender = "Male"
		self.weapons = "Fusil d'assault"
		self.weapons2 = "Mini-Gun"
		self.qi = "90"
		self.resistance = "70"

	def __str__(self):
		return "Taille  : " + self.taille + " Mètre | Poids : " + self.poids + " Kg | QI : " + self.qi + " | Résistance : " + self.resistance

	def dessin(self):
		print("                       ______ ")
		print("                     <((((((\\\  ")
		print("                     /      . }\ ")
		print("                     ;--..--._|} ")
		print("  (\                 '--/\--'  ) ")
		print("   \\                | '-'  :'|  ")
		print("    \\               . -==- .-|  ")
		print("     \\               \.__.'   \--._")
		print("     [\\          __.--|       //  _/'--.")
		print("     \ \\       .'-._ ('-----'/ __/      \ ")
		print("      \ \\     /   __>|      | '--.       | ")

