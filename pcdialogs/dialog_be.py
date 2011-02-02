import dialog , operator
from functools import partial                
from myfunctools import changeArg, changeReturnValue
from decorator import decorator

@decorator
def wrapper(f, self, args):
    MAX_LINES = 4
    MAX_LINE_LENGTH = 100
    # max line count/length
    args.message = ''.join( [x[:MAX_LINE_LENGTH] for x,_ in zip(args.message.splitlines(1) , range(MAX_LINES)) ])
        
    if not len(args.get('choices', [])):
        args.choices = ['']
    return f(self, args)
    
class Backend():
    def __init__(self):
        self.dlg =dialog.Dialog()
        
        handleReturn = partial(changeReturnValue, funcOnReturn = lambda ((i,s)): s if i==0 else None)

        # missing defaults
        self.dlg.fselect = partial(handleReturn(self.dlg.fselect), height=8,  width=60)

        self.dlg.menu = handleReturn(changeArg(self.dlg.menu, choices= lambda choices : [ (x,'') for x in choices]))
            
        # TODO: default
        self.dlg.checklist = handleReturn(changeArg(self.dlg.checklist, choices= lambda choices : [ (x,'', 0) for x in choices]))
            
        self.dlg.yesno = changeReturnValue(self.dlg.yesno, operator.__not__)
        self.dlg.inputbox = handleReturn(self.dlg.inputbox)
        self.dlg.passwordbox = handleReturn(self.dlg.passwordbox)

##[[[cog
##   import apigen
##   apigen.generateBackend('dialog', 'self.dlg', 'wrapper')
##]]]
## for cog indent
    
    @wrapper
    def message(self, args):
        """generated function"""
        return self.dlg.msgbox(text=args.message, title=args.title)
## for cog indent
    
    @wrapper
    def askString(self, args):
        """generated function"""
        return self.dlg.inputbox(init=args.default, text=args.message, title=args.title)
## for cog indent
    
    @wrapper
    def askPassword(self, args):
        """generated function"""
        return self.dlg.passwordbox(init=args.default, text=args.message, title=args.title)
## for cog indent
    
    @wrapper
    def askFileForOpen(self, args):
        """generated function"""
        return self.dlg.fselect(filepath=args.default, title=args.title)
## for cog indent
    
    @wrapper
    def askFileForSave(self, args):
        """generated function"""
        return self.dlg.fselect(filepath=args.default, title=args.title)
## for cog indent
    
    @wrapper
    def askFolder(self, args):
        """generated function"""
        return self.dlg.fselect(filepath=args.default, title=args.ok)
## for cog indent
    
    @wrapper
    def choice(self, args):
        """generated function"""
        return self.dlg.menu(text=args.message, title=args.title, choices=args.choices)
## for cog indent
    
    @wrapper
    def multiChoice(self, args):
        """generated function"""
        return self.dlg.checklist(text=args.message, title=args.title, choices=args.choices)
## for cog indent
    
    @wrapper
    def text(self, args):
        """generated function"""
        return self.dlg.scrollbox(text=args.text, title=args.title)
## for cog indent
    
    @wrapper
    def askYesNo(self, args):
        """generated function"""
        return self.dlg.yesno(text=args.message, title=args.title)
## for cog indent
    
    @wrapper
    def startProgress(self, args):
        """generated function"""
        return self.dlg.gauge_start(text=args.message, percent=args.percentage, title=args.title)
    
    @wrapper
    def stopProgress(self, args):
        """generated function"""
        return self.dlg.gauge_stop()
##[[[end]]] 

