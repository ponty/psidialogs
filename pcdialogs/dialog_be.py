import dialog , operator
from functools import partial                
from myfunctools import changeArg, changeReturnValue
#from decorator import decorator

#@decorator
def wrapper(f, self, args):
    MAX_LINES = 4
    MAX_LINE_LENGTH = 100
    # max line count/length
    args.message = ''.join( [x[:MAX_LINE_LENGTH] for x,_ in zip(args.message.splitlines(1) , range(MAX_LINES)) ])
        
    if not len(args.get('choices', [])):
        args.choices = ['']
    return f(self, args)
    
class Backend():
    ubuntu_package='python-dialog'
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

    @wrapper
    def message(self, args):
        """generated function"""
        return self.dlg.msgbox(text=args.message, title=args.title)
    
    @wrapper
    def ask_string(self, args):
        """generated function"""
        return self.dlg.inputbox(init=args.default, text=args.message, title=args.title)
    
    @wrapper
    def ask_file(self, args):
        """generated function"""
        return self.dlg.fselect(filepath=args.default, title=args.title)
    
    @wrapper
    def ask_folder(self, args):
        """generated function"""
        return self.dlg.fselect(filepath=args.default, title=args.ok)
    
    @wrapper
    def choice(self, args):
        """generated function"""
        return self.dlg.menu(text=args.message, title=args.title, choices=args.choices)
    
    @wrapper
    def multi_choice(self, args):
        """generated function"""
        return self.dlg.checklist(text=args.message, title=args.title, choices=args.choices)
    
    @wrapper
    def text(self, args):
        """generated function"""
        return self.dlg.scrollbox(text=args.text, title=args.title)
    
    @wrapper
    def ask_yes_no(self, args):
        """generated function"""
        return self.dlg.yesno(text=args.message, title=args.title)

