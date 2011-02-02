import easygui

class Backend():        
    def version(self):
        return str(easygui.egversion)
        
    def message(self, args):        
        return easygui.msgbox(msg=args.message, ok_button=args.ok, title=args.title)
    
    def askString(self, args):        
        return easygui.enterbox(default=args.default, msg=args.message, title=args.title)
    
    def askPassword(self, args):        
        return easygui.passwordbox(argDefaultPassword=args.default, message=args.message, title=args.title)
    
    def askFileForOpen(self, args):        
        return easygui.fileopenbox(default=args.default, msg=args.message, title=args.title)
    
    def askFileForSave(self, args):        
        return easygui.filesavebox(default=args.default, msg=args.message, title=args.title)
    
    def askFolder(self, args):        
        return easygui.diropenbox(default=args.default, msg=args.message, title=args.title)
    
    def choice(self, args):    
        return easygui.choicebox(msg=args.message, title=args.title, choices=args.choices)
    
    def multiChoice(self, args):    
        return easygui.multchoicebox(message=args.message, title=args.title, choices=args.choices)
    
    def text(self, args):        
        return easygui.textbox(text=args.text, msg=args.message, title=args.title)
    
    def askYesNo(self, args):       
        return easygui.ynbox(msg=args.message, title=args.title)
    
    def buttonChoice(self, args):
        return easygui.buttonbox(msg=args.message, title=args.title, choices=args.choices)

    
        
