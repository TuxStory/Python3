#!/usr/bin/python3

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Déciaml", "Binaire", "Octadécimal", "Hexadécimal"]

for i in range (16):
	b = bin(i)
	o = oct(i)
	h = hex(i)
	x.add_row([i,b[2:],o[2:],h[2:]])

x.align["Binaire"] = "r"
print(x.get_string(title="Tableau de nombres"))

#The issue is that you are using the prettytable package (c. 2013) and not the PTable package (c. 2015).
#Both provide the prettytable module. Only the PTable package supports table titles.
#pip3 install PTable

#--------------------------------------------
#mytable.add_column("Column1", [my_list_a[0], my_list_a[1], my_list_a[2])
#as
#
#mytable.add_column("Column1",[ item in item for mylist ])
#--------------------------------------------
