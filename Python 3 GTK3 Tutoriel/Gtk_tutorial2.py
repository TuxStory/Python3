import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")

        #bouton
        self.bouton = Gtk.Button(label="Ok")
        self.bouton.connect("clicked",self.bouton_clique)
        self.add(self.bouton)

    def bouton_clique(self, widget):
        print("Ok! Ca marche")


window = MainWindow()
#window = Gtk.Window(title="ApplicationX")
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
