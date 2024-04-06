#!/usr/bin/python

import os

def Affiche(itemsDict, leftWidth, rightWidth):
    print(' Users '.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

def Affiche2(Name,Tab, Tab2, leftWidth, rightWidth):
    print ("="*(leftWidth+rightWidth))
    print (Name.center(leftWidth + rightWidth))
    print ("="*(leftWidth+rightWidth))
    for i in range(len(Tab)):
        print(Tab[i].ljust(leftWidth, '.') + str(Tab2[i]).rjust(rightWidth))
    print ()

def main():
    print ("Nothing here.")

if __name__=="__main__":
    main()
