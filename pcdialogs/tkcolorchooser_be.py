import tkColorChooser
from Tkinter import Tk

class Backend():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        ##        FIXME: parent=self.root,

##[[[cog
##   import apigen
##   apigen.generateBackend('tkcolorchooser', 'tkColorChooser', )
##]]]
## for cog indent
    
    def askColor(self, args):
        """generated function"""
        return tkColorChooser.askcolor(color=args.default, title=args.title)
##[[[end]]] 
