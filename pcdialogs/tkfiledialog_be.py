import tkFileDialog
##from decorator import decorator
from Tkinter import Tk

##@decorator            
##def convertResult(func, self, args):
##    result = func(self, args)
##    if func.__name__=='choice':
##        if result and result.accepted:
##            return result.selection

class Backend():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        #  FIXME: parent?

##[[[cog
##   import apigen
##   apigen.generateBackend('tkfiledialog', 'tkFileDialog')
##]]]
## for cog indent
    
    def askFileForOpen(self, args):
        """generated function"""
        return tkFileDialog.askopenfilename()
## for cog indent
    
    def askFileForSave(self, args):
        """generated function"""
        return tkFileDialog.asksaveasfilename()
## for cog indent
    
    def askFolder(self, args):
        """generated function"""
        return tkFileDialog.askdirectory()
## for cog indent
    
    def askFilesForOpen(self, args):
        """generated function"""
        return tkFileDialog.askopenfilenames()
##[[[end]]] 
