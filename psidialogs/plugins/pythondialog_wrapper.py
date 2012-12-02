from psidialogs.unicodeutil import ansi_dialog
from psidialogs.iplugin import IPlugin


MAX_LINES = 4
MAX_LINE_LENGTH = 100


class Backend(IPlugin):
    backend = 'Python Dialog'
    ubuntu_package = 'python-dialog'
    url = 'http://pythondialog.sourceforge.net/'
    console = True
    name = 'pythondialog'

    def __init__(self):
        import dialog
        self.dlg = dialog.Dialog()

    def backend_version(self):
        return 'not implemented'

    @ansi_dialog
    def message(self, args):
        self.dlg.msgbox(text=args.message, title=args.title)

    @ansi_dialog
    def ask_string(self, args):
        (i, s) = self.dlg.inputbox(init=args.default, text=args.message, title=args.title)
        return s if i == 0 else None

    @ansi_dialog
    def ask_file(self, args):
        (i, s) = self.dlg.fselect(filepath=args.default, title=args.title, height=8, width=60)
        return s if i == 0 else None

    def ask_folder(self, args):
        return self.ask_file(args)

    @ansi_dialog
    def choice(self, args):
        if not len(args.get('choices', [])):
            args.choices = ['']
        choices = [ (x, '') for x in args.choices]
        (i, s) = self.dlg.menu(text=args.message, title=args.title, choices=choices)
        return s if i == 0 else None

    @ansi_dialog
    def multi_choice(self, args):
        choices = [ (x, '', 0) for x in args.choices]
        (i, s) = self.dlg.checklist(text=args.message, title=args.title, choices=choices)
        return s if i == 0 else None

    @ansi_dialog
    def text(self, args):
#        args.message = ''.join([x[:MAX_LINE_LENGTH] for x, _ in zip(args.message.splitlines(1) , range(MAX_LINES)) ])
        self.dlg.scrollbox(text=args.text, title=args.title)

    @ansi_dialog
    def ask_yes_no(self, args):
        return not self.dlg.yesno(text=args.message, title=args.title)

    @ansi_dialog
    def ask_ok_cancel(self, args):
        # TODO: set button labels
        return not self.dlg.yesno(text=args.message, title=args.title,
                                  # ok_label='OK',
                                  # cancel='Cancel',
                                  )

