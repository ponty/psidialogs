"""
url = 'http://pythondialog.sourceforge.net/'
"""

from psidialogs.iplugin import IPlugin

MAX_LINES = 4
MAX_LINE_LENGTH = 100


class PythonDialogWrapper(IPlugin):
    console = True
    name = "pythondialog"

    def __init__(self):
        import dialog

        self.dlg = dialog.Dialog()

    def backend_version(self):
        return "not implemented"

    def message(self, message, title):
        self.dlg.msgbox(text=message, title=title)

    def ask_string(self, message, title):
        (i, s) = self.dlg.inputbox(
            # init=args["default"],
            text=message,
            title=title,
        )
        return s if i == "ok" else None

    def ask_file(self, message, title):
        (i, s) = self.dlg.fselect(
            # filepath=args["default"],
            title=title,
            height=8,
            width=60,
        )
        return s if i == "ok" else None

    def ask_folder(self, message, title):
        return self.ask_file(message, title)

    def choice(self, choices, message, title):
        # if not len(args.get("choices", [])):
        #     args["choices"] = [""]
        choices = [(x, "") for x in choices]
        (i, s) = self.dlg.menu(text=message, title=title, choices=choices)
        return s if i == "ok" else None

    # def multi_choice(self, args):
    #     choices = [(x, "", 0) for x in args["choices"]]
    #     (i, s) = self.dlg.checklist(
    #         text=message, title=title, choices=choices
    #     )
    #     return s if i == "ok" else None

    # def text(self, args):
    #     # args['message'] = ''.join([x[:MAX_LINE_LENGTH] for x, _ in
    #     # zip(args['message'].splitlines(1) , range(MAX_LINES)) ])
    #     self.dlg.scrollbox(text=args["text"], title=title)

    def ask_yes_no(self, message, title):
        x = self.dlg.yesno(text=message, title=title,)
        return x == "ok"

    def ask_ok_cancel(self, message, title):
        x = self.dlg.yesno(
            text=message, title=title, yes_label="OK", no_label="Cancel",
        )
        return x == "ok"
