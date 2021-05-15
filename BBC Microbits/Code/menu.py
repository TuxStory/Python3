# Add your Python code here. E.g.

from microbit import *

def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
    Carre = [carre,carre2,carre3,carre2]
    for i in range(5):
        display.show(Carre, delay=200)
    display.clear()
    
def carre2():
    for i in range(10):
        for x in range(5):
            display.set_pixel(x,0,9)
            sleep(100)
        for y in range(5):
            display.set_pixel(x,y,9)
            sleep(100)
        for x in range(5):
            display.set_pixel(4-x,y,9)
            sleep(100)
        for y in range(5):
            display.set_pixel(0,4-y,9)
            sleep(100)
        display.clear()    
        
def arrows():
    for i in range(5):
        display.show(Image.ALL_ARROWS,delay=100)
    display.clear()

def boutons():
    display.scroll("Test button")
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.scroll("AB")
            break
        elif button_a.is_pressed():
               display.scroll("A")
        elif button_b.is_pressed():
            display.scroll("B")
        sleep(100)

def K2000():
    display.scroll("K2000")
    for i in range(30):
            for x in range(1,5):
                display.set_pixel(x-1,2,5)
                display.set_pixel(x,2,9)
                sleep(100)
                display.clear()
            for x in range(1,4):
                display.set_pixel(4-x,2,9)
                display.set_pixel(4-x+1,2,5)
                sleep(100)
                display.clear()  

def main():
    display.scroll("A to select")
    while True:
        sleep(3000) 
        count = button_a.get_presses()
        display.scroll(str(count))

        #Shake
        if accelerometer.was_gesture("shake"):
            display.scroll("Pas si fort !")
        
        #count
        if count == 1:
            display.scroll(str(temperature())+"C")
        elif count == 2:
            carre()
        elif count == 3:
            carre2()
        elif count == 4:
            arrows()
        elif count == 5:
            boutons()
        elif count == 6:
            K2000()
        #remise à zero    
        count = 0

if __name__=="__main__":
    main()
            