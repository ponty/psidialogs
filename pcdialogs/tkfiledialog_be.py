import tkFileDialog
from Tkinter import Tk

class Backend():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        #  FIXME: parent?

    def ask_file(self, args):
        """generated function"""
        if args.save:
            return tkFileDialog.asksaveasfilename()
        else:
            return tkFileDialog.askopenfilename()
    
    def ask_folder(self, args):
        """generated function"""
        return tkFileDialog.askdirectory()
    
    def ask_files(self, args):
        """generated function"""
        return tkFileDialog.askopenfilenames()
