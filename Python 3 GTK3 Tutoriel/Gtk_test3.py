import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")

        self.set_size_request(400,400)
        #sc = gtk.ScrolledWindow()
        lo = Gtk.Layout()
        lo.set_size(400,400)

        #label
        self.label1 = Gtk.Label(label="Nom :")
        self.label2 = Gtk.Label(label="Prenom :")
        self.label3 = Gtk.Label(label="Profession :")
        self.label4 = Gtk.Label(label="Age:")
        self.label5 = Gtk.Label(label="Anniversaire :")
        self.label6 = Gtk.Label(label="Ville :")
        self.label7 = Gtk.Label(label="Taille :")
        self.label8 = Gtk.Label(label="Telephone :")
        self.label9 = Gtk.Label(label="Permis :")
        self.label10 = Gtk.Label(label="E-mail :")

        #Entry
        self.NOM = Gtk.Entry()
        self.PRENOM = Gtk.Entry()
        self.PROFESSION = Gtk.Entry()
        self.AGE = Gtk.Entry()
        self.DATEN = Gtk.Entry()
        self.VILLE = Gtk.Entry()
        self.TAILLE = Gtk.Entry()
        self.TELEPHONE = Gtk.Entry()
        self.PERMIS = Gtk.Entry()
        self.EMAIL = Gtk.Entry()

        self.bouton = Gtk.Button(label="Ajouter")
        self.bouton.connect("clicked",self.bouton_clique)

        #Placement des elements
        lo.put(self.label1, 10, 15)
        lo.put(self.label2, 10, 45)
        lo.put(self.label3, 10, 75)
        lo.put(self.label4, 10, 105)
        lo.put(self.label5, 10, 135)
        lo.put(self.label6, 10, 165)
        lo.put(self.label7, 10, 195)
        lo.put(self.label8, 10, 225)
        lo.put(self.label9, 10, 255)
        lo.put(self.label10, 10, 285)

        lo.put(self.NOM, 120, 10)
        lo.put(self.PRENOM,120, 40)
        lo.put(self.PROFESSION,120, 70)
        lo.put(self.AGE,120, 100)
        lo.put(self.DATEN,120, 130)
        lo.put(self.VILLE,120, 160)
        lo.put(self.TAILLE,120, 190)
        lo.put(self.TELEPHONE,120, 220)
        lo.put(self.PERMIS,120, 250)
        lo.put(self.EMAIL,120, 280)

        lo.put(self.bouton,320 ,360)

        #Ajout Layout
        self.add(lo)

    def bouton_clique(self, widget):
        print("Ok! Ca marche")

window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
