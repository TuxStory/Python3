#!/usr/bin/python

import csv
from affichage import Affiche2

Name = []
Number = []

with open('ubuntu.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        Name.append(row[0])
        Number.append(row[2])

Affiche2("Ubuntu",Number,Name,20,10)
