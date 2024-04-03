#!/bin/usr/python

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + s - 96) % 26 + 96)
    return result

text = input("Phrase à encoder : ")
s = int(input("Nombre de décalage/clé : "))
print(encrypt(text,s))
