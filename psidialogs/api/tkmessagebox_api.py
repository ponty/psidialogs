import psidialogs

def askokcancel(title=None, message=None, **options):
    """Original doc: Ask if operation should proceed; return true if the answer is ok"""
    return psidialogs.ask_ok_cancel(title=title, message=message)

def showinfo(title=None, message=None, **options):
    """Original doc: Show an info message"""
    return psidialogs.message(title=title, message=message)

def askyesno(title=None, message=None, **options):
    """Original doc: Ask a question; return true if the answer is yes"""
    return psidialogs.ask_yes_no(title=title, message=message)

def showwarning(title=None, message=None, **options):
    """Original doc: Show a warning message"""
    return psidialogs.warning(title=title, message=message)

def showerror(title=None, message=None, **options):
    """Original doc: Show an error message"""
    return psidialogs.error(title=title, message=message)

def askretrycancel(title=None, message=None, **options):
    """Original doc: Ask if operation should be retried; return true if the answer is yes"""
    return psidialogs.ask_ok_cancel(title=title, message=message, ok='Retry')

def askquestion(title=None, message=None, **options):
    if askyesno(title=title, message=message):
        return 'yes'
    else:
        return 'no'
