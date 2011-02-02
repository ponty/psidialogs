import tkMessageBox
from Tkinter import Tk, TkVersion


class Backend():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        ##        FIXME: parent=self.root,
    
    def version():
        return str(TkVersion)

##[[[cog
##   import apigen
##   apigen.generateBackend('tkmessagebox', 'tkMessageBox', )
##]]]
## for cog indent
    
    def message(self, args):
        """generated function"""
        return tkMessageBox.showinfo(message=args.message, title=args.title)
## for cog indent
    
    def error(self, args):
        """generated function"""
        return tkMessageBox.showerror(message=args.message, title=args.title)
## for cog indent
    
    def warning(self, args):
        """generated function"""
        return tkMessageBox.showwarning(message=args.message, title=args.title)
## for cog indent
    
    def askOkCancel(self, args):
        """generated function"""
        return tkMessageBox.askokcancel(message=args.message, title=args.title)
## for cog indent
    
    def askYesNo(self, args):
        """generated function"""
        return tkMessageBox.askyesno(message=args.message, title=args.title)
## for cog indent
    
##[[[end]]] 
