#!/usr/bin/python3.7

import os
import re

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def test():
	for i in range(20):
		print (i,end=" ")
	print ()
	print ("-"*50)

def question():
	Q1 = input(bcolors.OKBLUE+"Would you like to play a game? (o/n) : "+bcolors.ENDC)
	if Q1 == "o":
		print (bcolors.BOLD + "The only winning move is not to play" + bcolors.ENDC)
	if Q1 == "n":
		print ("You are wise !")
	print("-"*50)

def Tablo():
	Linux = ['Debian','Ubuntu','Kali','Fedora','Archlinux']
	Linux.append('Slitaz')
	Linux.sort()
	print (Linux)
	print ("-"*50)

def liens():
	os.system("curl -L www.debian.org -o test.txt")
	with open("test.txt") as file:
		for line in file:
			# (https?:\/\/|www\.)[a-zA-Z0-9-_\.\/\?=&]+iso <- devrait être ça
			urls = re.findall('https?://[a-zA-Z0-9-_\.\/\?=&]+iso', line)
			if (urls) != []:
			#print (urls[0])
				os.system("wget "+(urls[0]))
				#Si plus de un Résultat il faudra gérer ça

def fonction(num):
	x=num*num
	return x

def main():
	os.system("clear")
	print ("Hello World")
	print ("-"*50)
	print (os.getcwd())
	print ("-"*50)
	os.system('ls -lah')
	print ("-"*50)
	test()
	question()
	Tablo()
	os.system("uname -a")
	print("-"*50)
	#os.system("htop ")
	#liens()
	#os.system("hexchat")
	print (fonction(5))

if __name__=="__main__":
	main()

