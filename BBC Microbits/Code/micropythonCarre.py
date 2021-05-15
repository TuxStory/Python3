from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
                
carre = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999:")
              
carre2 = Image("00000:"
               "09090:"
               "09090:"
               "09990:"
               "00000:")

carre2 = Image("00000:"
               "09090:"
               "09090:"
               "09990:"
               "00000:")

carre3 = Image("00000:"
               "00000:"
               "00900:"
               "00000:"
               "00000:")
               
display.show(mystery)
sleep(100)
display.scroll("Carre")
for i in range(5):
    display.show(carre)
    sleep(100)
    display.show(carre2)
    sleep(100)
    display.show(carre3)
    sleep(100)

--------------------------------------------------------------------------------

from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()
    
def main():
    display.show(mystery)
    sleep(500)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed():
            carre()

main()
--------------------------------------------------------------------------------

from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()

def carre2():
    for x in range(5):
        display.set_pixel(x,0,9)
        sleep(200)
    for y in range(5):
        display.set_pixel(4,y,9)
        sleep(200)
    for x in range(5):
        display.set_pixel(4-x,4,9)
        sleep(200)
    for y in range(5):
        display.set_pixel(0,4-y,9)
        sleep(200)
    display.clear()

def main():
    display.show(mystery)
    sleep(300)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed():
            carre()
        if button_b.is_pressed():
            carre2()

main()
-------------------------------------------------------------------------------
from microbit import *

mystery = Image('00300:'
                '03630:'
                '36963:'
                '03630:'
                '00300')
def carre():
    carre = Image("99999:90009:90009:90009:99999:")
    carre2 = Image("00000:09990:09090:09990:00000:")
    carre3 = Image("00000:00000:00900:00000:00000:")
             
    for i in range(10):
        display.show(carre)
        sleep(300)
        display.show(carre2)
        sleep(300)
        display.show(carre3)
        sleep(300)
        display.clear()

def carre2():
    for i in range(5):
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
        

def main():
    display.show(mystery)
    sleep(300)
    display.scroll("Carre ?")
    display.clear()
    while True:
        if button_a.is_pressed():
            carre()
        if button_b.is_pressed():
            carre2()

main()

