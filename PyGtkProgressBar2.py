import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
   
def progress_timeout(pbobj):
   new_val = pbobj.pb.get_fraction() + 0.01
   pbobj.pb.set_fraction(new_val)
   pbobj.pb.set_text(str(new_val*100)+" % completed")
   return True

class PyApp(Gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Progressbar demo")
      self.set_size_request(300,200)
      #self.set_position(Gtk.WIN_POS_CENTER)
		
      fix = Gtk.Fixed()
      self.pb = Gtk.ProgressBar()
      self.pb.set_text("Progress")
      self.pb.set_fraction(0.0)
		
      fix.put(self.pb,80,100)
      self.add(fix)
      self.timer = gobject.timeout_add (100, progress_timeout, self)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
PyApp()
gtk.main()