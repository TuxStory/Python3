import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")
        self.set_size_request(200,10)
        self.set_border_width(10)

        #Boxes
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(self.box)

        #Box2
        self.box2 = Gtk.Box(spacing=6)
        self.box.pack_start(self.box2,True,True,0)

        #Label NAME
        self.label = Gtk.Label()
        self.label.set_label("Votre Nom :")
        self.box2.pack_start(self.label,True,True,0)

        #Entry NAME
        self.NAME = Gtk.Entry()
        self.box2.pack_start(self.NAME,True,True,0)

        #Box2
        self.box3 = Gtk.Box(spacing=6)
        self.box.pack_start(self.box3,True,True,0)

        #Label NAME
        self.label2 = Gtk.Label()
        self.label2.set_label("Votre Prenom :")
        self.box3.pack_start(self.label2,True,True,0)

        #Entry FIRSTNAME
        self.FIRSTNAME = Gtk.Entry()
        self.box3.pack_start(self.FIRSTNAME,True,True,0)

        #Box4
        self.box4 = Gtk.Box(spacing=6)
        self.box.pack_start(self.box4,True,True,0)

        #Label Ville
        self.label3 = Gtk.Label()
        self.label3.set_label("Votre Ville :")
        self.box4.pack_start(self.label3,True,True,0)

        #Entry Ville
        self.VILLE = Gtk.Entry()
        self.box4.pack_start(self.VILLE,True,True,0)

        #Box5
        self.box5 = Gtk.Box(spacing=6)
        self.box.pack_start(self.box5,True,True,0)

        #bouton
        self.bouton = Gtk.Button(label="Ok")
        self.bouton.connect("clicked",self.bouton_clique)
        self.box5.pack_start(self.bouton,True,True,0)

    def bouton_clique(self, widget):
        Name = self.NAME.get_text()
        FirstName = self.FIRSTNAME.get_text()
        Ville = self.VILLE.get_text()
        print("Infos : ",Name,FirstName,Ville)


window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
