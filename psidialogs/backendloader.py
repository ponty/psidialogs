from psidialogs.loader import PluginLoader
from psidialogs.singl import singleton


default_preference = """
easygui
zenity
wxpython
gmessage
tkinter
pygtk
pyqt
pythondialog
console
""".strip().splitlines()


@singleton
class BackendLoader(PluginLoader):
    def __init__(self):
        PluginLoader.__init__(self, default_preference)

    def is_console(self, name):
        return name in ["console", "pythondialog"]
