#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")
        self.set_border_width(10)
        self.set_icon_from_file("tux.png")

        #Boxes
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        #bouton & entry
        self.Cbouton = Gtk.CheckButton(label="Ceci est un test", use_underline=True)
        self.bouton = Gtk.Button(label="Enoyer")
        self.bouton.connect("clicked",self.bouton_clique)
        self.Cbouton.set_active(True)
        self.box.pack_start(self.Cbouton,True,True,0)
        self.box.pack_start(self.bouton,True,True,0)

    def bouton_clique(self, widget):
	    status = self.Cbouton.get_active()
	    print(status)

window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
