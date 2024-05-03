#!/usr/bin/python

class Planet(object):
  def __init__(self, name, typ, order):
    self.name = name
    self.typ = typ
    self.order = order

  def describe_planet(self):
    return "This is %s, a%s. It is the %s planet from the sun." % (self.name, self.typ, self.order)


if __name__ == '__main__':

  mercure = Planet("Mercure", "  planete", "1st")
  venus = Planet("Venus", " planete terrestre", "2nd")
  terre = Planet("Terre", " planete terrestre", "3rd")
  mars = Planet("Mars", " panete terrestre", "4th")
  jupiter = Planet("Jupiter", " gas giant", "5th")
  saturne = Planet("Saturne", " gas giant", "6th")
  uranus = Planet("Uranus", "n ice giant", "7th")
  neptune = Planet("Neptune", "n ice giant", "8th")

  print (terre.describe_planet())
