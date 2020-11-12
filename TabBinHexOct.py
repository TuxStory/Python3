#!/usr/bin/python3.5

for i in range (16):
	b = bin(i)
	o = oct(i)
	h = hex(i)
	print( "|",i,"|",b[2:],"|",o[2:],"|",h[2:],"|")

