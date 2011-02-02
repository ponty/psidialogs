import tkSimpleDialog
from Tkinter import Tk

class Backend():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        ##        FIXME: parent=self.root,

##[[[cog
##   import apigen
##   apigen.generateBackend('tksimpledialog', 'tkSimpleDialog', )
##]]]
## for cog indent
    
    def ask_string(self, args):
        """generated function"""
        return tkSimpleDialog.askstring(prompt=args.message, title=args.title)
## for cog indent
    
##[[[end]]] 
