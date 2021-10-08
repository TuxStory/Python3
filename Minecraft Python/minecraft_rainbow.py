import mcpi.minecraft as minecraft
import mcpi.block as block

import time,math

mc = minecraft.Minecraft.create()
mc.postToChat("Rainbow World")
pos = mc.player.getTilePos()
print (pos)
#red, orange,yellow,green,blue,indigo,violet
rainbow = [14,1,4,13,11,10,2]
radius = 30

for angle in range(360):
  for i in range(len(rainbow)):
    x = pos.x + (radius - i) * math.cos(angle*math.pi/180)
    y = 0 + (radius - i) * math.sin(angle*math.pi/180)
    mc.setBlock(x,y,pos.z,block.WOOL.id,rainbow[i])
    #time.sleep(0.1)
