#!/bin/python3

import os, time, cursor

#Colors
GREEN = '\033[92m'
ENDC = '\033[0m'
#Texte
txt = "Wake up, Neo..."
txt2 = "The Matrix has you...\nFollow the white rabbit.\nKnock, knock, Neo\n"
txt3 = "(\ /)\n(-.-)\n"

def flush(txt):
    for i in range(0,len(txt)):
        print(GREEN+txt[i]+ENDC,end="", flush=True)
        time.sleep(0.20)

def main():
    cursor.hide()
    os.system("clear")
    flush(txt)
    os.system("clear")
    flush(txt2)
    os.system("clear")
    print(txt3)
    cursor.show()
main()
