import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")

        #Boxes
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        #Bouton1
        self.bouton1 = Gtk.Button(label="Debian")
        self.bouton1.connect("clicked",self.bouton1_clique)
        self.box.pack_start(self.bouton1,True,True,0)

        #bouton2
        self.bouton2 = Gtk.Button(label="Ubuntu")
        self.bouton2.connect("clicked",self.bouton2_clique)
        self.box.pack_start(self.bouton2,True,True,0)

    def bouton1_clique(self,widget):
        print("Bon Choix!")

    def bouton2_clique(self,widget):
        print("C'est aussi un bon choix")


window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
