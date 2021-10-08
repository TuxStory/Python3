from mcpi import minecraft, block
from time import sleep

mc = minecraft.Minecraft.create()
mc.postToChat("Hello World!")

#Pos = mc.player.getPos()
x,y,z = mc.player.getPos()
print ("Position X: ",x)
print ("Position y: ",y)
print ("Position z: ",z)

#Centre de la map
mc.player.setPos(0,0,0)
mc.postToChat("Jump !")
mc.player.setPos(x,y+100,z)

#block
mc.setBlock(x+1,y,z,1)
mc.setBlock(x+5,y,z,block.MELON.id)

#blocks
mc.setBlocks(x+5,y+5,z+5,x+16,y+16,z+16,3)
mc.setBlocks(x,y,z,x+5,y+5,z+5,46,1) #TNT 1=Explosive

grass = 2
flower = 38

while True:
  x, y, z = mc.player.getPos()  # player position (x, y, z)
  block_beneath = mc.getBlock(x, y-1, z)  # block ID
  #print(block_beneath)

  if block_beneath == grass:
    mc.setBlock(x, y, z, flower)
  sleep(0.1)

#https://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/
#AIR                   0
#STONE                 1
#GRASS                 2
#DIRT                  3
#COBBLESTONE           4
#WOOD_PLANKS           5
#SAPLING               6
#BEDROCK               7
#WATER_FLOWING         8
#WATER                 8
#WATER_STATIONARY      9
#LAVA_FLOWING         10
#LAVA                 10
#TNT                  46