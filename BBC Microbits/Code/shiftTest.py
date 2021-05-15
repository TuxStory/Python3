from microbit import *

I = Image("00000:09990:09990:09990:00000")
display.show(I)
for i in range(2):
    I = I.shift_left(1)
    display.show(I)
    sleep(400)
for i in range(2):
    I = I.shift_right(1)
    display.show(I)
    sleep(400)
display.clear()

display.show(Image.HEART)
sleep(400)
H = Image.HEART
for i in range(5):
    H = H.shift_down(1)
    display.show(H)
    sleep(400)