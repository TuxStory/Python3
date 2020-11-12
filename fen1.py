#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

fenetre = Tk()

l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="yes")


label = Label(fenetre, text="Hello World")
label.pack()

label1 = Label(fenetre, text="Texte par défaut", bg="yellow")
label1.pack()

#value = StringVar() 
#value.set("texte par défaut")
#entree = Entry(fenetre, textvariable=String, width=30)
#entree.pack()

bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
 
Label(l, text="A l'intérieure de la frame").pack()


fenetre.mainloop()
