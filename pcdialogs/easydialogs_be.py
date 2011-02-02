import easydialogs
from myfunctools import changeArg, changeReturnValue
from functools import partial                

# returns [()] by cancel
funcOnReturn = lambda x: x if x else None
easygui.diropenbox = changeReturnValue( easygui.diropenbox, funcOnReturn)
easygui.fileopenbox = changeReturnValue( easygui.fileopenbox, funcOnReturn)

# min/max mandatory 
def handleLimit(x, typ):
    if x is None or x=='':
        if typ=='max':
            x = 100000000
        elif typ=='min':
            x = -100000000
        else:
            raise
    return x
easygui.integerbox = changeArg(easygui.integerbox, argLowerBound=partial(handleLimit, typ='min'), argUpperBound=partial(handleLimit, typ='max'))
# cancel -> ''
easygui.integerbox = changeReturnValue(easygui.integerbox, lambda x: x if x!='' else None )

# 0,1 (int)
easygui.ynbox = changeReturnValue( easygui.ynbox, bool)

# 'OK'
easygui.msgbox = changeReturnValue( easygui.msgbox, lambda x: None)
easygui.textbox = changeReturnValue( easygui.textbox, lambda x: None)

class Backend():        
##[[[cog
##   import apigen
##   apigen.generateBackend('easydialogs', 'easydialogs')
##]]]
## for cog indent
    
    def message(self, args):
        """generated function"""
        return easygui.msgbox(message=args.message, buttonMessage=args.ok, title=args.title)
## for cog indent
    
    def askString(self, args):
        """generated function"""
        return easygui.enterbox(argDefaultText=args.default, message=args.message, title=args.title)
## for cog indent
    
    def askPassword(self, args):
        """generated function"""
        return easygui.passwordbox(argDefaultPassword=args.default, message=args.message, title=args.title)
## for cog indent
    
    def askFileForOpen(self, args):
        """generated function"""
        return easygui.fileopenbox(argInitialFile=args.default, msg=args.message, title=args.title)
## for cog indent
    
    def askFileForSave(self, args):
        """generated function"""
        return easygui.filesavebox(argInitialFile=args.default, msg=args.message, title=args.title)
## for cog indent
    
    def askFolder(self, args):
        """generated function"""
        return easygui.diropenbox(argInitialDir=args.default, msg=args.message, title=args.title)
## for cog indent
    
    def choice(self, args):
        """generated function"""
        return easygui.choicebox(message=args.message, title=args.title, choices=args.choices)
## for cog indent
    
    def multiChoice(self, args):
        """generated function"""
        return easygui.multchoicebox(message=args.message, title=args.title, choices=args.choices)
## for cog indent
    
    def text(self, args):
        """generated function"""
        return easygui.textbox(text=args.text, message=args.message, title=args.title)
## for cog indent
    
    def askYesNo(self, args):
        """generated function"""
        return easygui.ynbox(message=args.message, title=args.title)
## for cog indent
    
    def buttonChoice(self, args):
        """generated function"""
        return easygui.buttonbox(message=args.message, title=args.title, choices=args.choices)
##[[[end]]] 

    
        
