from yapsy.IPlugin import IPlugin
import wx.lib.dialogs
#import wx

            
class Backend(IPlugin):
    backend='wxPython'
    backend_version=wx.__version__
    
    def __init__(self):
        self.app = None
        
    def init(self):
        if not self.app:
            self.app = wx.App()

    def message(self, args):        
        self.init()
        wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CENTRE)
    
    def warning(self, args):        
        self.init()
        wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CENTRE | wx.ICON_WARNING)
    
    def error(self, args):
        self.init()
        wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CENTRE | wx.ICON_ERROR)
##        wx.lib.dialogs.alertDialog(message=args.message, title=args.title)

    def ask_ok_cancel(self, args):
        self.init()
        result = wx.lib.dialogs.messageDialog(message=args.message, title=args.title, 
                                              aStyle = wx.OK | wx.CANCEL | wx.CENTRE 
                                              )
        return result.accepted
    
    def ask_yes_no(self, args):
        self.init()
        result = wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.YES | wx.NO | wx.CENTRE| wx.YES_DEFAULT)
        return result.accepted
    
    def ask_string(self, args):
        self.init()
        result = wx.lib.dialogs.textEntryDialog(defaultText=args.default, message=args.message, title=args.title)
        if result and result.accepted:
            return result.text
    

    def ask_file(self, args):
        self.init()
        if args.save:
            result = wx.lib.dialogs.saveFileDialog(filename=args.default, title=args.title)
        else:
            result = wx.lib.dialogs.openFileDialog(filename=args.default, title=args.title, style=wx.OPEN )
        if result and result.accepted:
            if len(result.paths):
                return result.paths[0]
    
    def ask_folder(self, args):
        self.init()
        # no effect: message=args.message
        result = wx.lib.dialogs.directoryDialog(path=args.default)
        if result and result.accepted:
            return result.path
    
#    def button_choice(self, args):
#        # TODO: create dialog
#        return self.choice(args)

    def choice(self, args):
        self.init()
        result = wx.lib.dialogs.singleChoiceDialog(message=args.message, title=args.title, lst=args.choices)
        if result and result.accepted:
            return result.selection
    
    def multi_choice(self, args):
        self.init()
        result = wx.lib.dialogs.multipleChoiceDialog(message=args.message, title=args.title, lst=args.choices)
        if result and result.accepted:
            return list(result.selection)

    def text(self, args):
        self.init()
        wx.lib.dialogs.scrolledMessageDialog(message=args.text, title=args.title)

