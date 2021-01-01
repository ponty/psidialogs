from psidialogs import mixins
from psidialogs.iplugin import IPlugin


class TkinterWrapper(IPlugin):
    root = None
    name = "tkinter"

    def __init__(self):
        from tkinter import Tk
        import tkinter
        from tkinter import messagebox, filedialog, simpledialog

        self.Tk = Tk
        self.Tkinter = tkinter
        self.tkFileDialog = filedialog
        self.tkMessageBox = messagebox
        self.tkSimpleDialog = simpledialog

    def backend_version(self):
        return str(self.Tkinter.TkVersion)

    def tk_init(self):
        if not self.root:
            self.root = self.Tk()
            self.root.withdraw()

    def ask_string(self, args):
        self.tk_init()
        return self.tkSimpleDialog.askstring(
            prompt=args["message"], title=args["title"]
        )

    def message(self, args):
        self.tk_init()
        self.tkMessageBox.showinfo(message=args["message"], title=args["title"])

    def error(self, args):
        self.tk_init()
        self.tkMessageBox.showerror(message=args["message"], title=args["title"])

    def warning(self, args):
        self.tk_init()
        self.tkMessageBox.showwarning(message=args["message"], title=args["title"])

    def ask_ok_cancel(self, args):
        self.tk_init()
        return self.tkMessageBox.askokcancel(
            message=args["message"], title=args["title"]
        )

    def ask_yes_no(self, args):
        self.tk_init()
        return self.tkMessageBox.askyesno(message=args["message"], title=args["title"])

    def ask_file(self, args):
        self.tk_init()
        # if args["save"]:
        #     x = self.tkFileDialog.asksaveasfilename()
        # else:
        x = self.tkFileDialog.askopenfilename()
        if not x:
            x = None
        return x

    def ask_folder(self, args):
        self.tk_init()
        x = self.tkFileDialog.askdirectory()
        if not x:
            x = None
        return x

    def choice(self, args):
        return mixins.choice(self, args)

    def multi_choice(self, args):
        return mixins.multi_choice(self, args)
