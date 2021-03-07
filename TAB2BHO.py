#!/usr/bin/python3.8

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Déciaml", "Binaire", "Octadécimal", "Hexadécimal"]

for i in range (16):
	b = bin(i)
	o = oct(i)
	h = hex(i)
	x.add_row([i,b[2:],o[2:],h[2:]])

#print(x)
x.align["Binaire"] = "r"
print(x.get_string(title="Tableau de nombres"))

#--------------------------------------------
#mytable.add_column("Column1", [my_list_a[0], my_list_a[1], my_list_a[2])
#as
#
#mytable.add_column("Column1",[ item in item for mylist ])
#--------------------------------------------
