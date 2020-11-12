#!/usr/bin/env python2
# -*- coding: utf8 -*-

import irclib
import ircbot
from math import *

class BotChallenge(ircbot.SingleServerIRCBot):
	i = True
	def __init__(self):
		# on se connecte au serveur
		ircbot.SingleServerIRCBot.__init__(self, [("irc.root-me.org", 6667)],"challenge_python", "challenge_python")

	def on_welcome(self, serv, ev):
		# on envoie un message privé à Candy
		serv.privmsg("Candy", "!ep1")

	def on_privmsg(self, serv, ev):
		# ici on reçoit la réponse de Candy que l'on récupère dans la variable chaine
		chaine = ev.arguments()[0]
		print chaine

		# i indique si la réponse a déjà été envoyé. Si c'est le cas cette partie
		# ne doit plus être interprétée
		if(self.i):
			# On effectue quelques opérations de base pour récupérer les nombres sans / ou .
			# et on fait les calculs nécessaires
			chaine = chaine.split('/')
			result = sqrt(int(chaine[0]))
			chaine = chaine[1].split('.')
			result = round(result * int(chaine[0]), 2)
			# Une fois qu'on a tout, il ne reste plus qu'à envoyer la réponse à Candy
			# et à attendre le mot de passe
			cmd = "!ep1 -rep " + str(result)
			serv.privmsg("Candy", cmd)
			
			print 'result = %f'%result
			self.i = False

if __name__ == "__main__":
	BotChallenge().start()