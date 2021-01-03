from psidialogs.iplugin import IPlugin


class Choices:
    def __init__(self, tkinter, parent, choicelist, message):
        self.parent = parent
        self.choice = None
        tkinter.Label(parent, text=message).grid(
            row=0, column=0, columnspan=2, sticky="W"
        )

        self.var = tkinter.StringVar()
        self.var.set(choicelist[0])
        popupMenu = tkinter.OptionMenu(parent, self.var, *choicelist)
        popupMenu.grid(
            sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W,
            row=1,
            column=0,
            columnspan=2,
        )

        tkinter.Button(parent, text="OK", command=self.button_ok).grid(row=2, column=0)
        tkinter.Button(parent, text="Cancel", command=self.button_cancel).grid(
            row=2, column=1
        )

    def button_ok(self):
        self.choice = self.var.get()
        self.parent.quit()

    def button_cancel(self):
        self.parent.quit()


class TkinterWrapper(IPlugin):
    root = None
    name = "tkinter"

    def __init__(self):
        from tkinter import Tk
        import tkinter
        from tkinter import messagebox, filedialog, simpledialog

        self.Tk = Tk
        self.tkinter = tkinter
        self.filedialog = filedialog
        self.messagebox = messagebox
        self.simpledialog = simpledialog

    def backend_version(self):
        return str(self.tkinter.TkVersion)

    def tk_init(self):
        if not self.root:
            self.root = self.Tk()
            self.root.withdraw()

    def ask_string(self, args):
        self.tk_init()
        return self.simpledialog.askstring(prompt=args["message"], title=args["title"])

    def message(self, args):
        self.tk_init()
        self.messagebox.showinfo(message=args["message"], title=args["title"])

    def error(self, args):
        self.tk_init()
        self.messagebox.showerror(message=args["message"], title=args["title"])

    def warning(self, args):
        self.tk_init()
        self.messagebox.showwarning(message=args["message"], title=args["title"])

    def ask_ok_cancel(self, args):
        self.tk_init()
        return self.messagebox.askokcancel(message=args["message"], title=args["title"])

    def ask_yes_no(self, args):
        self.tk_init()
        return self.messagebox.askyesno(message=args["message"], title=args["title"])

    def ask_file(self, args):
        self.tk_init()
        # if args["save"]:
        #     x = self.tkFileDialog.asksaveasfilename()
        # else:
        x = self.filedialog.askopenfilename()
        if not x:
            x = None
        return x

    def ask_folder(self, args):
        self.tk_init()
        x = self.filedialog.askdirectory()
        if not x:
            x = None
        return x

    def choice(self, args):
        gui = self.Tk()
        gui.resizable(False, False)
        gui.title(args["title"])
        app = Choices(self.tkinter, gui, args["choices"], args["message"])
        gui.mainloop()
        return app.choice
        # return mixins.choice(self, args)

    # def multi_choice(self, args):
    #     return mixins.multi_choice(self, args)
