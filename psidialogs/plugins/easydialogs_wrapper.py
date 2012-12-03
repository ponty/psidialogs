from psidialogs.unicodeutil import ansi_dialog
from psidialogs.iplugin import IPlugin


class Backend(IPlugin):
    backend = 'EasyDialogs'
    name = 'easydialogs'

    def __init__(self):
        import EasyDialogs
        self.EasyDialogs = EasyDialogs

    @ansi_dialog
    def ask_string(self, args):
        return self.EasyDialogs.AskString(prompt=args.message, default=args.default)

    @ansi_dialog
    def message(self, args):
        self.EasyDialogs.Message(args.message)

    @ansi_dialog
    def ask_ok_cancel(self, args):
        x = self.EasyDialogs.AskYesNoCancel(
            question=args.message, default=args.default, yes='OK', no='')
        return x == 1

    @ansi_dialog
    def ask_yes_no(self, args):
        x = self.EasyDialogs.AskYesNoCancel(
            question=args.message, default=args.default, cancel='')
        return x == 1

    @ansi_dialog
    def ask_file(self, args):
        if args.save:
            x = self.EasyDialogs.AskFileForSave(
                message=args.message, defaultLocation=args.default)
        else:
            x = self.EasyDialogs.AskFileForOpen(
                message=args.message, defaultLocation=args.default)
        return x

    @ansi_dialog
    def ask_folder(self, args):
        x = self.EasyDialogs.AskFolder(
            message=args.message, defaultLocation=args.default)
        return x
