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
        self.root = None
        
    def tk_init(self):
        if not self.root:
            self.root = Tk()
            self.root.withdraw()
        
    def ask_string(self, args):
        self.tk_init()
        return tkSimpleDialog.askstring(prompt=args.message, title=args.title)

    def message(self, args):
        self.tk_init()
        tkMessageBox.showinfo(message=args.message, title=args.title)
    
    def error(self, args):
        self.tk_init()
        tkMessageBox.showerror(message=args.message, title=args.title)
    
    def warning(self, args):
        self.tk_init()
        tkMessageBox.showwarning(message=args.message, title=args.title)
    
    def ask_ok_cancel(self, args):
        self.tk_init()
        return tkMessageBox.askokcancel(message=args.message, title=args.title)
    
    def ask_yes_no(self, args):
        self.tk_init()
        return tkMessageBox.askyesno(message=args.message, title=args.title)

    def ask_file(self, args):
        self.tk_init()
        if args.save:
            x= tkFileDialog.asksaveasfilename()
        else:
            x= tkFileDialog.askopenfilename()
        if not x:
            x=None
        return x
    
    def ask_folder(self, args):
        self.tk_init()
        x= tkFileDialog.askdirectory()
        if not x:
            x=None
        return x
    
