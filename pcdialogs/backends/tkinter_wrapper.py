from Tkinter import Tk
from yapsy.IPlugin import IPlugin
import Tkinter
import tkFileDialog
import tkMessageBox
import tkSimpleDialog

class Backend(IPlugin):
    backend='TkInter'
    backend_version = str(Tkinter.TkVersion)
    
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        
    def ask_string(self, args):
        return tkSimpleDialog.askstring(prompt=args.message, title=args.title)

    def message(self, args):
        tkMessageBox.showinfo(message=args.message, title=args.title)
    
    def error(self, args):
        tkMessageBox.showerror(message=args.message, title=args.title)
    
    def warning(self, args):
        tkMessageBox.showwarning(message=args.message, title=args.title)
    
    def ask_ok_cancel(self, args):
        return tkMessageBox.askokcancel(message=args.message, title=args.title)
    
    def ask_yes_no(self, args):
        return tkMessageBox.askyesno(message=args.message, title=args.title)

    def ask_file(self, args):
        if args.save:
            x= tkFileDialog.asksaveasfilename()
        else:
            x= tkFileDialog.askopenfilename()
        if not x:
            x=None
        return x
    
    def ask_folder(self, args):
        x= tkFileDialog.askdirectory()
        if not x:
            x=None
        return x
    
    def ask_files(self, args):
        x= tkFileDialog.askopenfilenames()
        x=list(x)
        if not len(x):
            x=None
        return x
