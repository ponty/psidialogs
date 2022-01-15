from psidialogs.iplugin import IPlugin


class EasyguiWrapper(IPlugin):
    name = "easygui"

    def __init__(self):
        import easygui  # type: ignore

        self.easygui = easygui

    def backend_version(self):
        return self.easygui.egversion

    def message(self, message, title):
        self.easygui.msgbox(msg=message, title=title)

    def warning(self, message, title):
        self.message(message, title)

    def error(self, message, title):
        self.message(message, title)

    def ask_string(self, message, title):
        return self.easygui.enterbox(
            # default=args["default"],
            msg=message,
            title=title,
        )

    def ask_file(self, message, title):
        # if args["save"]:
        #     return self.easygui.filesavebox(
        #         # default=args["default"],
        #         msg=message,
        #         title=title,
        #     )
        # else:
        return self.easygui.fileopenbox(
            # default=args["default"],
            msg=message,
            title=title,
        )

    def ask_folder(self, message, title):
        return self.easygui.diropenbox(
            # default=args["default"],
            msg=message,
            title=title,
        )

    def choice(self, choices, message, title):
        return self.easygui.choicebox(msg=message, title=title, choices=choices)

    # def multi_choice(self, args):
    #     return self.easygui.multchoicebox(
    #         msg=message, title=title, choices=args["choices"]
    #     )

    # def text(self, args):
    #     self.easygui.textbox(
    #         text=args["text"], msg=message, title=title
    #     )

    def ask_yes_no(self, message, title):
        x = self.easygui.ynbox(msg=message, title=title)
        return bool(x)

    def ask_ok_cancel(self, message, title):
        x = self.easygui.ynbox(msg=message, title=title, choices=("OK", "Cancel"))
        return bool(x)


#    def button_choice(self, args):
# return easygui.buttonbox(msg=args['message'], title=args['title'],
# choices=args['choices'])
