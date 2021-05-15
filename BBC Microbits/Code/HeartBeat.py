from microbit import *
import music

while True:
    if accelerometer.was_gesture("shake"):
        display.show(random.randint(1,6))
        sleep(400)
    display.show(Image.HEART)
    sleep(300)
    display.show(Image.HEART_SMALL)
    sleep(300)
    note=["C4:4"]
    music.play(note)

#NOTE[octave][:duration]