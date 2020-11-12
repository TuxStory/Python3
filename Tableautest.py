#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits.count('apple'))
fruits.append("peach")

for fruit in fruits:
	print(fruit,end=" ")

print()
fruits.reverse()
print(fruits)
fruits.append('grape')
fruits.extend(("poire","pomme"))
fruits.sort()

for fruit in fruits:
	print(fruit,end=" ")

print()
