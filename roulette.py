#!/usr/bin/env python

#NOTE A REFAIRE COMPLETEMENT .... 
# -*- coding: utf-8 -*-
#
#  roulette.py
#
#  Copyright 2017 antoine <antoine@localhost.localdomain>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

def main(args):

#Variables

	print("Casino : Roulette")
	NUMERO = input("Choississez un numéro [0-36] : ")
	MISE = input("Entrez votre mise : ")
	MISE = int(MISE)
	NUMERO = int(NUMERO)

	def roulette():
		import random
		numero_gagnant = random.randint(0,36)
		return numero_gagnant

	def couleur(NUMERO,numero):
		if (NUMERO % 2 == 0 and numero % 2 == 0):
			return True
		elif (NUMERO % 2 != 0 and numero % 2 != 0):
			return True
		else:
			print("Aie ! Vous n'avez pas non plus la bonne couleur")
		return False

#jeu
	numero = roulette()
	print("Les jeux sont faits !")
	print("Le numero gagnant est le : ", numero)
	if NUMERO == numero:
		print("Bravo ! vous avez gagné !")
		print("Vous remportez la somme de :", MISE*33, "Euros")
	elif NUMERO != numero:
		print("Vous avez perdu")
		coul = couleur(NUMERO,numero)
		if coul == True:
			print("Vous avez la bonne couleur.")
			print("vous gagnez la somme de",MISE/2, "Euros")

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
