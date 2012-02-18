from psidialogs.unicodeutil import ansi_dialog
from yapsy.IPlugin import IPlugin
import EasyDialogs

class Backend(IPlugin):
    backend = 'EasyDialogs'
#    backend_version = ?
    
    @ansi_dialog
    def ask_string(self, args):
        return EasyDialogs.AskString(prompt=args.message, default=args.default)

    @ansi_dialog
    def message(self, args):
        EasyDialogs.Message(args.message)
    
    @ansi_dialog
    def ask_ok_cancel(self, args):
        x = EasyDialogs.AskYesNoCancel(question=args.message, default=args.default, yes='OK', no='')
        return x==1
    
    @ansi_dialog
    def ask_yes_no(self, args):
        x = EasyDialogs.AskYesNoCancel(question=args.message, default=args.default, cancel='')
        return x==1
        
    @ansi_dialog
    def ask_file(self, args):
        if args.save:
            x = EasyDialogs.AskFileForSave(message=args.message, defaultLocation=args.default)
        else:
            x = EasyDialogs.AskFileForOpen(message=args.message, defaultLocation=args.default)
        return x
    
    @ansi_dialog
    def ask_folder(self, args):
        x = EasyDialogs.AskFolder(message=args.message, defaultLocation=args.default)
        return x
    
