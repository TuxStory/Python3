import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")
        
        #Boxes
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        #bouton & entry
        self.bouton = Gtk.Button(label="test")
        self.case = Gtk.Entry()
        self.bouton.connect("clicked",self.bouton_clique)
        self.case.set_text("Texte")
        self.box.pack_start(self.case,True,True,0)
        self.box.pack_start(self.bouton,True,True,0)
        

    def bouton_clique(self, widget):
	    txt = self.case.get_text()
	    print(txt)


window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
