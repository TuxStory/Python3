from microbit import *

img = Image(5,5)

for j in range(10):
    for i in range(5):
        img.set_pixel(i,i,9)
        display.show(img)
        sleep(500)
        img.set_pixel(i,i,0)
    display.clear()
    for i in range(3):
        img.set_pixel(3-i,3-i,9)
        display.show(img)
        sleep(500)
        img.set_pixel(3-i,3-i,0)
    display.clear()

'''
test = [1,4,2,2,4,3,4,0,2,1,0,4,3]
for i in test():
    img.set_pixel((test[2]),(test[5]),9)
    display.show(img)
    sleep(100)
    display.clear()
'''