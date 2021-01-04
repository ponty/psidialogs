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

    def ask_string(self, message, title):
        self.tk_init()
        return self.simpledialog.askstring(prompt=message, title=title)

    def message(self, message, title):
        self.tk_init()
        self.messagebox.showinfo(message=message, title=title)

    def error(self, message, title):
        self.tk_init()
        self.messagebox.showerror(message=message, title=title)

    def warning(self, message, title):
        self.tk_init()
        self.messagebox.showwarning(message=message, title=title)

    def ask_ok_cancel(self, message, title):
        self.tk_init()
        return self.messagebox.askokcancel(message=message, title=title)

    def ask_yes_no(self, message, title):
        self.tk_init()
        return self.messagebox.askyesno(message=message, title=title)

    def ask_file(self, message, title):
        self.tk_init()
        # if args["save"]:
        #     x = self.tkFileDialog.asksaveasfilename()
        # else:
        x = self.filedialog.askopenfilename(title=title)
        if not x:
            x = None
        return x

    def ask_folder(self, message, title):
        self.tk_init()
        x = self.filedialog.askdirectory(title=title)
        if not x:
            x = None
        return x

    def choice(self, choices, message, title):
        gui = self.Tk()
        w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
        x, y = int((w / 2) - 200), int((h / 2) - 200)
        gui.geometry("+{}+{}".format(x, y))

        gui.resizable(False, False)
        gui.title(title)
        app = Choices(self.tkinter, gui, choices, message)
        gui.mainloop()
        return app.choice
        # return mixins.choice(self, args)

    # def multi_choice(self, args):
    #     return mixins.multi_choice(self, args)
