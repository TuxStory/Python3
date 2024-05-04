#!/usr/bin/python

class Planet(object):
  def __init__(self, name, typ, order, rayon, distancesol):
    self.name = name
    self.typ = typ
    self.order = order
    self.rayon = rayon
    self.distancesol = distancesol

  def describe_planet(self):
    return "Nom : %s\nType :  %s\nPosition : %s\nRayon : %s\nDistance soleil : %s" % (self.name, self.typ, self.order, self.rayon ,self.distancesol)

if __name__ == '__main__':

  mercure = Planet("Mercure", "Planète tellurique", "1", "2439", "58")
  venus = Planet("Venus", "Planète tellurique", "2", "6051", "108,2")
  terre = Planet("Terre", "Planète tellurique", "3", "6371", "149,6")
  mars = Planet("Mars", "Planète tellurique", "4", "3389", "225")
  jupiter = Planet("Jupiter", "Géante gazeuse", "5", "69911", "778,5")
  saturne = Planet("Saturne", "Géante gazeuse", "6", "58232", "1434")
  uranus = Planet("Uranus", " Géante de glace", "7", "25362", "2871")
  neptune = Planet("Neptune", "Géante de glace", "8", "24662", "4495")

  sysolaire = [mercure,venus,terre,mars,jupiter,saturne,uranus,neptune]
  for planet in sysolaire:
    print (planet.describe_planet())
    print ("========================")
