from psidialogs.iplugin import IPlugin

# macos:  brew install wxpython
# ubuntu 20.04: crash in qt after wx if app is destroyed
app = None


class WxPythonWrapper(IPlugin):
    name = "wxpython"

    def __init__(self):
        import wx.lib.dialogs  # type: ignore

        self.wx = wx

    def backend_version(self):
        return self.wx.__version__

    def init(self):
        global app
        if not app:
            app = self.wx.App()

    def message(self, message, title):
        self.init()
        self.wx.lib.dialogs.messageDialog(
            message=message,
            title=title,
            aStyle=self.wx.OK | self.wx.CENTRE,
        )

    def warning(self, message, title):
        self.init()
        self.wx.lib.dialogs.messageDialog(
            message=message,
            title=title,
            aStyle=self.wx.OK | self.wx.CENTRE | self.wx.ICON_WARNING,
        )

    def error(self, message, title):
        self.init()
        self.wx.lib.dialogs.messageDialog(
            message=message,
            title=title,
            aStyle=self.wx.OK | self.wx.CENTRE | self.wx.ICON_ERROR,
        )

    # #        self.wx.lib.dialogs.alertDialog(message=args['message'], title=args['title'])

    def ask_ok_cancel(self, message, title):
        self.init()
        result = self.wx.lib.dialogs.messageDialog(
            message=message,
            title=title,
            aStyle=self.wx.OK | self.wx.CANCEL | self.wx.CENTRE,
        )
        return result.accepted

    def ask_yes_no(self, message, title):
        self.init()
        result = self.wx.lib.dialogs.messageDialog(
            message=message,
            title=title,
            aStyle=self.wx.YES | self.wx.NO | self.wx.CENTRE | self.wx.YES_DEFAULT,
        )
        return result.accepted

    def ask_string(self, message, title):
        self.init()
        result = self.wx.lib.dialogs.textEntryDialog(
            # defaultText=args["default"],
            message=message,
            title=title,
        )
        if result and result.accepted:
            return result.text

    def ask_file(self, message, title):
        self.init()
        # if args["save"]:
        #     result = self.wx.lib.dialogs.saveFileDialog(
        #         # filename=args["default"],
        #         title=title,
        #     )
        # else:
        result = self.wx.lib.dialogs.openFileDialog(
            # filename=args["default"],
            title=title,
            style=self.wx.FD_OPEN,
        )
        if result and result.accepted:
            if len(result.paths):
                return result.paths[0]

    def ask_folder(self, message, title):
        self.init()
        # no effect: message=args['message']
        result = self.wx.lib.dialogs.directoryDialog()  # path=args["default"])
        if result and result.accepted:
            return result.path

    #    def button_choice(self, args):
    #        # TODO: create dialog
    #        return self.choice(args)

    def choice(self, choices, message, title):
        self.init()
        result = self.wx.lib.dialogs.singleChoiceDialog(
            message=message, title=title, lst=choices
        )
        if result and result.accepted:
            return result.selection

    # def multi_choice(self, args):
    #     self.init()
    #     result = self.wx.lib.dialogs.multipleChoiceDialog(
    #         message=message, title=title, lst=args["choices"]
    #     )
    #     if result and result.accepted:
    #         return list(result.selection)

    # def text(self, args):
    #     self.init()
    #     self.wx.lib.dialogs.scrolledMessageDialog(
    #         message=args["text"], title=title
    #     )
