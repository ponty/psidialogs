import easygui
from yapsy.IPlugin import IPlugin

class Backend(IPlugin):        
    backend='EasyGui'
    backend_version=easygui.egversion
    
    def message(self, args):        
        easygui.msgbox(msg=args.message, title=args.title)
    
    def ask_string(self, args):        
        return easygui.enterbox(default=args.default, msg=args.message, title=args.title)
    
    def ask_file(self, args):        
        if args.save:
            return easygui.filesavebox(default=args.default, msg=args.message, title=args.title)
        else:
            return easygui.fileopenbox(default=args.default, msg=args.message, title=args.title)

    def ask_folder(self, args):        
        return easygui.diropenbox(default=args.default, msg=args.message, title=args.title)
    
    def choice(self, args):    
        return easygui.choicebox(msg=args.message, title=args.title, choices=args.choices)
    
    def multi_choice(self, args):    
        return easygui.multchoicebox(msg=args.message, title=args.title, choices=args.choices)
    
    def text(self, args):        
        easygui.textbox(text=args.text, msg=args.message, title=args.title)
    
    def ask_yes_no(self, args):       
        x= easygui.ynbox(msg=args.message, title=args.title)
        return bool(x)
    
    def ask_ok_cancel(self, args):       
        x= easygui.ynbox(msg=args.message, title=args.title, choices=("OK", "Cancel"))
        return bool(x)
    
#    def button_choice(self, args):
#        return easygui.buttonbox(msg=args.message, title=args.title, choices=args.choices)

    
        
