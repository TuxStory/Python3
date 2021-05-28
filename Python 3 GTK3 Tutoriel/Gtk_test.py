import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ApplicationX")

        #bouton
        self.dlg = Gtk.ColorChooserDialog("test")
        #self.dlg.connect(self.on_color)
        self.add(self.dlg)
        
    def on_color(self, widget):
        dlg = gtk.ColorSelectionDialog("Select color")
        col = dlg.run()
        sel = dlg.colorsel.get_current_color()
        self.text.modify_fg(gtk.STATE_NORMAL, sel)

    #"def bouton_clique(self, widget):
      #  print("Ok! Ca marche")


window = MainWindow()
#window = Gtk.Window(title="ApplicationX")
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
