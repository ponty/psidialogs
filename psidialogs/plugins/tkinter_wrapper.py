from psidialogs.util import platform_is_osx, platform_is_win, platform_is_linux
from psidialogs.iplugin import IPlugin

# macos:  brew install python-tk

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


root = None


class TkinterWrapper(IPlugin):
    name = "tkinter"
    need_subprocess = platform_is_osx()

    def __init__(self):
        import tkinter
        from tkinter import Tk, filedialog, messagebox, simpledialog

        self.Tk = Tk
        self.tkinter = tkinter
        self.filedialog = filedialog
        self.messagebox = messagebox
        self.simpledialog = simpledialog

    def backend_version(self):
        return str(self.tkinter.TkVersion)

    def tk_init(self):
        global root
        if not root:
            root = self.Tk()
            # root.overrideredirect(1)
            root.withdraw()

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
        self.tk_init()
        root.update()
        root.deiconify()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        x, y = int((w / 2) - 100), int((h / 2) - 100)
        root.geometry("+{}+{}".format(x, y))

        root.resizable(False, False)
        root.title(title)
        app = Choices(self.tkinter, root, choices, message)
        root.mainloop()
        root.withdraw()

        return app.choice

    # def multi_choice(self, args):
    #     return mixins.multi_choice(self, args)
