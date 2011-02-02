import backend_api

def message(message='Hello!', ok='OK', title=''):
    """generated function"""
    return backend_api.opendialog("message" , dict(message=message, ok=ok, title=title))
def text(text='', message='', title=''):
    """generated function"""
    return backend_api.opendialog("text" , dict(text=text, message=message, title=title))
def error(message='Error!', ok='OK', title=''):
    """generated function"""
    return backend_api.opendialog("error" , dict(message=message, ok=ok, title=title))
def warning(message='Warning!', ok='OK', title=''):
    """generated function"""
    return backend_api.opendialog("warning" , dict(message=message, ok=ok, title=title))
def ask_string(message='Enter something.', default='', ok='OK', cancel='Cancel', title=''):
    """generated function"""
    return backend_api.opendialog("ask_string" , dict(message=message, default=default, ok=ok, cancel=cancel, title=title))
def ask_file(message='Select file for open.', default='', title='', save=False):
    """generated function"""
    return backend_api.opendialog("ask_file" , dict(message=message, default=default, title=title, save=save))
def ask_files(message='Select files for open.', default='', title=''):
    """generated function"""
    return backend_api.opendialog("ask_files" , dict(message=message, default=default, title=title))
def ask_folder(message='Select folder.', default='', ok='OK', cancel='Cancel', title=''):
    """generated function"""
    return backend_api.opendialog("ask_folder" , dict(message=message, default=default, ok=ok, cancel=cancel, title=title))
def choice(choices=[], message='Pick something.', default=None, title=''):
    """generated function"""
    return backend_api.opendialog("choice" , dict(choices=choices, message=message, default=default, title=title))
def multi_choice(choices=[], message='Pick as many items as you like.', default=None, title=''):
    """generated function"""
    return backend_api.opendialog("multi_choice" , dict(choices=choices, message=message, default=default, title=title))
def button_choice(choices=[], message='Select a button.', default=0, title=''):
    """generated function"""
    return backend_api.opendialog("button_choice" , dict(choices=choices, message=message, default=default, title=title))
def ask_ok_cancel(message='', default=0, title=''):
    """generated function"""
    return backend_api.opendialog("ask_ok_cancel" , dict(message=message, default=default, title=title))
def ask_yes_no(message='', default=0, title=''):
    """generated function"""
    return backend_api.opendialog("ask_yes_no" , dict(message=message, default=default, title=title))

functions=[
           message,
           ask_string,
           ask_file, 
           ask_folder,
           choice,
           multi_choice, 
           text, 
           error,
           warning,
           ask_files,
           ask_ok_cancel,
           ask_yes_no,
           button_choice,           
           ]

function_names=[x.__name__ for x in functions]
