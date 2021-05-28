import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")

        grid = Gtk.Grid()
        self.add(grid)

        #creation de boutons
        bouton1 = Gtk.Button(label="Bouton 1")
        bouton2 = Gtk.Button(label="Bouton 2")
        bouton3 = Gtk.Button(label="Bouton 3")
        bouton4 = Gtk.Button(label="Bouton 4")
        bouton5 = Gtk.Button(label="Bouton 5")
        bouton6 = Gtk.Button(label="Bouton 6")

        grid.add(bouton1)
        grid.attach(bouton2, 1,0,2,1)
        grid.attach_next_to(bouton3, bouton1, Gtk.PositionType.BOTTOM,1, 2)
        grid.attach_next_to(bouton4, bouton3, Gtk.PositionType.RIGHT,2, 1)
        grid.attach(bouton5, 1, 2, 1, 1)
        grid.attach_next_to(bouton6, bouton5, Gtk.PositionType.RIGHT,1, 1)

window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
