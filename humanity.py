#!/usr/bin/pyhton3.5
#-*- coding: utf-8 -*-

class human:

	def __init__(self,nom,prenom,genre,age,peuple):
		self.nom = nom
		self.prenom = prenom
		self.genre = genre
		self.age = age
		self.vie = True
		self.peuple = peuple

	def affiche(self):
		print ("Je suis :", self.nom, self.prenom , end=' ')
		if self.genre == "Femme":
			print ("Je suis une", self.genre, "de", self.age, "ans.", end=' ')
		if self.genre ==  "Homme":
			print ("Je suis un", self.genre, "de", self.age, "ans.", end=' ')

	def vivant(self):
		if self.vie == True:
			print ("Je suis en vie.",end=" ")
		if self.vie == False:
			print ("Je suis mort.",end=" ")

	def patrie(self):
		print ("Ma patrie est :", self.peuple)

	def chromo(self):
		if self.genre == "Femme":
			gene = "x"
			return gene
		if self.genre == "Homme":
			import random
			gene = random.choice(['x','y'])
			return gene

