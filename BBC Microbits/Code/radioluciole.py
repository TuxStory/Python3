import radio
import random
from microbit import display, Image, button_a, sleep

# Création de la liste "flash" contenant les images de l'animation
# Comprends-tu comment ça fonctionne ?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# La radio ne marchera pas sauf si on l'allume !
radio.on()

# Boucle événementielle.
while True:
    # Le bouton A envoie un message "flash"
    if button_a.was_pressed():
        radio.send('flash')  # a-ha
    # On lit tous les messages entrant
    incoming = radio.receive()
    if incoming == 'flash':
        # Si il y a un message "flash" entrant
        # on affiche l'animation du flash de luciole après une petite
        # pause de durée aléatoire.
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        # On re-diffuse aléatoirement le message flash après une petite
        # pause
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')  # a-ha