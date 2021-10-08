from mcpi import minecraft, block
from time import sleep
from random import randint

mc = minecraft.Minecraft.create()
mc.postToChat("Pluie de sable")

for i in range(100):
  x,y,z = mc.player.getPos()
  n = randint(-10,10)
  mc.setBlock(x+n, y+20, z+n, 12)
  sleep(0.2)

mc.postToChat("C'est fini")
