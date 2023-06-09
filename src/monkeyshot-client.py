import sys
import gi
import os
from subprocess import Popen

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
        self.workingDir = "/home/" + os.getlogin() + "/.Monkeyshot"

    def on_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file(self.workingDir + "/assets/monkeyshot-client.ui")

        button = builder.get_object("sectionButton")
        button.connect("clicked", self.sectionButtonClicked)

        button = builder.get_object("fullscreenButton")
        button.connect("clicked", self.fullscreenButtonClicked)

        self.win = builder.get_object("main_window")
        self.win.set_application(self)
        self.win.present()

    def sectionButtonClicked(self, button):
        p = Popen(self.workingDir + '/assets/section.sh', shell=True)
        sys.exit()

    def fullscreenButtonClicked(self, button):
        p = Popen(self.workingDir + '/assets/fullscreen.sh', shell=True)
        sys.exit()

app = MyApp(application_id="")
app.run(sys.argv)
