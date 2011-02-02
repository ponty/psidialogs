from Tkinter import Tk
import tkFileDialog
import tkMessageBox
import tkSimpleDialog

class Backend():
    #version = Tkinter.TkVersion
    
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        
    def ask_string(self, args):
        """generated function"""
        return tkSimpleDialog.askstring(prompt=args.message, title=args.title)

    def message(self, args):
        """generated function"""
        return tkMessageBox.showinfo(message=args.message, title=args.title)
    
    def error(self, args):
        """generated function"""
        return tkMessageBox.showerror(message=args.message, title=args.title)
    
    def warning(self, args):
        """generated function"""
        return tkMessageBox.showwarning(message=args.message, title=args.title)
    
    def ask_ok_cancel(self, args):
        """generated function"""
        return tkMessageBox.askokcancel(message=args.message, title=args.title)
    
    def ask_yes_no(self, args):
        """generated function"""
        return tkMessageBox.askyesno(message=args.message, title=args.title)

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
