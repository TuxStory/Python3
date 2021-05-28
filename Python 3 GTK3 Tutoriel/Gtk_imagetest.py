import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")
        
        self.set_size_request(250,170)
        #sc = gtk.ScrolledWindow()
        lo = Gtk.Layout()
        lo.set_size(200,200)

        self.img = Gtk.Image()
        self.img.set_from_file("Python-logo.png")
        #self.add(self.img)
        lo.put(self.img,70,10)
        #bouton
        self.bouton = Gtk.Button(label="Python 3")
        self.bouton.connect("clicked",self.bouton_clique)
        #self.add(self.bouton)
        lo.put(self.bouton, 90, 130)
        self.add(lo)

    def bouton_clique(self, widget):
        print("Ok! Ca marche")
        self.img.set_from_file("tux.png")

window = MainWindow()
#window = Gtk.Window(title="ApplicationX")
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
