import wx.lib.dialogs 
import wx

_app = wx.App()
            
class Backend():
##[[[
##   import apigen
##   apigen.generateBackend('wxlibdialogs', 'wx.lib.dialogs')
##]]]
    def message(self, args):        
        wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CENTRE)
    
    def warning(self, args):        
        wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CENTRE | wx.ICON_WARNING)
    
    def error(self, args):
        wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CENTRE | wx.ICON_ERROR)
##        wx.lib.dialogs.alertDialog(message=args.message, title=args.title)

    def askOkCancel(self, args):
        result = wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.OK | wx.CANCEL | wx.CENTRE)
        return result.accepted
    
    def askYesNo(self, args):
        result = wx.lib.dialogs.messageDialog(message=args.message, title=args.title, aStyle = wx.YES | wx.NO | wx.CENTRE)
        return result.accepted
    
    def askString(self, args):
        result = wx.lib.dialogs.textEntryDialog(defaultText=args.default, message=args.message, title=args.title)
        if result and result.accepted:
            return result.text
    
    def askFilesForOpen(self, args):
        result = wx.lib.dialogs.openFileDialog(filename=args.default, title=args.title)
        if result and result.accepted:
            if len(result.paths):
                return result.paths

    def askFileForOpen(self, args):
        result = wx.lib.dialogs.openFileDialog(filename=args.default, title=args.title, style=wx.OPEN )
        if result and result.accepted:
            if len(result.paths):
                return result.paths[0]
    
    def askFileForSave(self, args):
        result = wx.lib.dialogs.saveFileDialog(filename=args.default, title=args.title)
        if result and result.accepted:
            if len(result.paths):
                return result.paths[0]
    
    def askFolder(self, args):
        # no effect: message=args.message
        result = wx.lib.dialogs.directoryDialog(path=args.default)
        if result and result.accepted:
            return result.path
    
    def choice(self, args):
        result = wx.lib.dialogs.singleChoiceDialog(message=args.message, title=args.title, lst=args.choices)
        if result and result.accepted:
            return result.selection
    
    def multiChoice(self, args):
        result = wx.lib.dialogs.multipleChoiceDialog(message=args.message, title=args.title, lst=args.choices)
        if result and result.accepted:
            return list(result.selection)

    def text(self, args):
        wx.lib.dialogs.scrolledMessageDialog(message=args.text, title=args.title)
##[[[end]]] 

