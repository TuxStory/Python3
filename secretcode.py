#!/usr/bin/python3

text = input("Phrase à encoder : ")

for c in text:
	x = ord(c)
	x = x + 14
	c2 = chr(x)
	print(c2, end=" ")

print()
