# Ecrit ton programme ici ;-)
import microbit

microbit.display.show(microbit.Image.HAPPY)
microbit.sleep(200)
microbit.display.clear()
microbit.compass.calibrate()

while True:
    needle = ((15 - microbit.compass.heading()) // 30) % 12
    microbit.display.show(microbit.Image.ALL_CLOCKS[needle])