#!/bin/python3

import os, time, cursor

#Colors
GREEN = '\033[92m'
ENDC = '\033[0m'

#Texte
txt = "Wake up, Neo..."
txt2 = "The Matrix has you...\nFollow the white rabbit.\nKnock, knock, Neo\n"
txt3 = "(\ /)\n(-.-)\n"
txt4 = """This is your last chance. After this, there is no turning back.\n
You take the blue pill - the story ends,
you wake up in your bed and believe whatever you want to believe.
You take the red pill - you stay in Wonderland and I show you how deep the rabbit hole goes."""
txt5 = "Ignorance is a bliss\n"

def flush(txt):
    for i in range(0,len(txt)):
        print(GREEN+txt[i]+ENDC,end="", flush=True)
        time.sleep(0.20)

def trinity():
    print(GREEN)
    os.system("nmap -A 192.168.1.1")
    print(ENDC)

def morpheus():
    flush(txt4)

def cypher():
    flush(txt5)

def browser():
    os.system("firefox --version")
    #os.system("chromium --version")

def main():
    cursor.hide()
    os.system("clear")
    flush(txt)
    os.system("clear")
    flush(txt2)
    os.system("clear")
    print(txt3)
    cursor.show()
    morpheus()
    os.system("clear")
    browser()
    cypher()
#    trinity()

if __name__=="__main__":
    main()
