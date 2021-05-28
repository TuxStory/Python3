import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.AboutDialog):

    def __init__(self):
        Gtk.AboutDialog.__init__(self, title="à propos de ...")
        self.set_website('http://www.test.be')
        self.set_program_name('Programme')
        self.set_logo_icon_name('applications-accessories')
#        self.set_logo(Pixbuf.new_from_file("Python-logo.png"))
        self.set_comments('Ceci est un programme de test\nDeveloppé en Python3')
        self.set_version('Version 0.2 -  11.06.2019 (BETA)')
        self.set_copyright('Antoine Even © 2019\nContact (test@gmail.com)')

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
