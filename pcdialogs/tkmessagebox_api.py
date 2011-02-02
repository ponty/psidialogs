import common_api

##[[[cog
##   import apigen
##   apigen.generateApi('tkmessagebox', 'tkMessageBox')
##]]]
def askokcancel(title=None, message=None, **options):
    """Original doc: Ask if operation should proceed; return true if the answer is ok"""
    return common_api.ask_ok_cancel(title=title, message=message)
def showinfo(title=None, message=None, **options):
    """Original doc: Show an info message"""
    return common_api.message(title=title, message=message)
def askyesno(title=None, message=None, **options):
    """Original doc: Ask a question; return true if the answer is yes"""
    return common_api.ask_yes_no(title=title, message=message)
def showwarning(title=None, message=None, **options):
    """Original doc: Show a warning message"""
    return common_api.warning(title=title, message=message)
def showerror(title=None, message=None, **options):
    """Original doc: Show an error message"""
    return common_api.error(title=title, message=message)
def askretrycancel(title=None, message=None, **options):
    """Original doc: Ask if operation should be retried; return true if the answer is yes"""
    return common_api.askRetryCancel(title=title, message=message)
##[[[end]]] 

def askquestion(title=None, message=None, **options):
    if askyesno(title=title, message=message):
        return 'yes'
    else:
        return 'no'
