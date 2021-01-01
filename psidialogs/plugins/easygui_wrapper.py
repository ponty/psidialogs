from psidialogs.iplugin import IPlugin


class EasyguiWrapper(IPlugin):
    name = "easygui"

    def __init__(self):
        import easygui

        self.easygui = easygui

    def backend_version(self):
        return self.easygui.egversion

    def message(self, args):
        self.easygui.msgbox(msg=args["message"], title=args["title"])

    def ask_string(self, args):
        return self.easygui.enterbox(
            # default=args["default"],
            msg=args["message"],
            title=args["title"],
        )

    def ask_file(self, args):
        # if args["save"]:
        #     return self.easygui.filesavebox(
        #         # default=args["default"],
        #         msg=args["message"],
        #         title=args["title"],
        #     )
        # else:
        return self.easygui.fileopenbox(
            # default=args["default"],
            msg=args["message"],
            title=args["title"],
        )

    def ask_folder(self, args):
        return self.easygui.diropenbox(
            # default=args["default"],
            msg=args["message"],
            title=args["title"],
        )

    def choice(self, args):
        return self.easygui.choicebox(
            msg=args["message"], title=args["title"], choices=args["choices"]
        )

    # def multi_choice(self, args):
    #     return self.easygui.multchoicebox(
    #         msg=args["message"], title=args["title"], choices=args["choices"]
    #     )

    # def text(self, args):
    #     self.easygui.textbox(
    #         text=args["text"], msg=args["message"], title=args["title"]
    #     )

    def ask_yes_no(self, args):
        x = self.easygui.ynbox(msg=args["message"], title=args["title"])
        return bool(x)

    def ask_ok_cancel(self, args):
        x = self.easygui.ynbox(
            msg=args["message"], title=args["title"], choices=("OK", "Cancel")
        )
        return bool(x)


#    def button_choice(self, args):
# return easygui.buttonbox(msg=args['message'], title=args['title'],
# choices=args['choices'])
