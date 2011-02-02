import backend_api
##[[[cog
##   import apigen
##   apigen.generateCommonAPI('backend_api.opendialog')
##]]]
def message(message='Hello!', ok='OK', title=''):
    """generated function"""
    return backend_api.opendialog("message" , dict(message=message, ok=ok, title=title))
def askString(message='Enter something.', default='', ok='OK', cancel='Cancel', title=''):
    """generated function"""
    return backend_api.opendialog("askString" , dict(message=message, default=default, ok=ok, cancel=cancel, title=title))
def askPassword(message='Enter password.', default='', ok='OK', cancel='Cancel', title=''):
    """generated function"""
    return backend_api.opendialog("askPassword" , dict(message=message, default=default, ok=ok, cancel=cancel, title=title))
def askFileForOpen(message='Select file for open.', default='', title=''):
    """generated function"""
    return backend_api.opendialog("askFileForOpen" , dict(message=message, default=default, title=title))
def askFileForSave(message='Select file for save.', default='', title=''):
    """generated function"""
    return backend_api.opendialog("askFileForSave" , dict(message=message, default=default, title=title))
def askFolder(message='Select folder.', default='', ok='OK', cancel='Cancel', title=''):
    """generated function"""
    return backend_api.opendialog("askFolder" , dict(message=message, default=default, ok=ok, cancel=cancel, title=title))
def choice(choices=[], message='Pick something.', default=None, title=''):
    """generated function"""
    return backend_api.opendialog("choice" , dict(choices=choices, message=message, default=default, title=title))
def multiChoice(choices=[], message='Pick as many items as you like.', default=None, title=''):
    """generated function"""
    return backend_api.opendialog("multiChoice" , dict(choices=choices, message=message, default=default, title=title))
def text(text='', message='', title=''):
    """generated function"""
    return backend_api.opendialog("text" , dict(text=text, message=message, title=title))
def error(message='Error!', ok='OK', title=''):
    """generated function"""
    return backend_api.opendialog("error" , dict(message=message, ok=ok, title=title))
def warning(message='Warning!', ok='OK', title=''):
    """generated function"""
    return backend_api.opendialog("warning" , dict(message=message, ok=ok, title=title))
def askFilesForOpen(message='Select files for open.', default='', title=''):
    """generated function"""
    return backend_api.opendialog("askFilesForOpen" , dict(message=message, default=default, title=title))
def askOkCancel(message='', default=0, title=''):
    """generated function"""
    return backend_api.opendialog("askOkCancel" , dict(message=message, default=default, title=title))
def askYesNo(message='', default=0, title=''):
    """generated function"""
    return backend_api.opendialog("askYesNo" , dict(message=message, default=default, title=title))
def askDate(message='Select date.', default='', title=''):
    """generated function"""
    return backend_api.opendialog("askDate" , dict(message=message, default=default, title=title))
def buttonChoice(choices=[], message='Select a button.', default=0, title=''):
    """generated function"""
    return backend_api.opendialog("buttonChoice" , dict(choices=choices, message=message, default=default, title=title))
##[[[end]]]
