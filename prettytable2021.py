#!/usr/bin/python3

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Numero", "Nom", "Package","Manager"]
Numero = range(5)
Name = ["Debian","Ubuntu","Linux Mint","Fedora","Red Hat","Manjaro"]
Package = ["deb","deb","deb","rpm","rpm","pkz"]
Manager = ["apt","apt","apt","dnf","dnf","pacman"]
for i in Numero:
    x.add_row([Numero[i],Name[i],Package[i],Manager[i]])

x.align["Nom"] = "l"
print (x)
#print(x.get_string(title="Test PrettyTable"))

## 2
columns = ["Student Name", "Class", "Section", "Percentage"] 
myTable = PrettyTable()
# Add Columns
myTable.add_column(columns[0], ["Leanord", "Penny", "Howard", "Bernadette", "Sheldon", "Raj", "Amy"])
myTable.add_column(columns[1], ["X", "X", "X", "X", "X", "X", "X"])
myTable.add_column(columns[2], ["B", "C", "A", "D", "A", "B", "B"])
myTable.add_column(columns[3], ["91.2 %", "63.5 %", "90.23 %", "92.7 %","98.2 %", "88.1 %", "95.0 %"])
print (myTable)
