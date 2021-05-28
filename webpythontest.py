import webbrowser

#webbrowser.open('http://inventwithpython.com/')
#ouvre une webbrowser à la page indiquée.

import webbrowser
address = input("Entrez une adresse Google Maps :")
webbrowser.open('https://www.google.com/maps/place/' + address)