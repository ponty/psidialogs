from psidialogs import ask_string, warning

def ask_float(message='Enter float.', default=0, ok='OK', cancel='Cancel', title=''):
    while 1:
        s = ask_string(message=message, default=unicode(default), ok=ok, cancel=cancel, title=title)
        if not s:
            return
        try:
            x=float(s)
            return x
        except:
            warning('"%s" is not a valid float!' % s, title=title)

    
def ask_int(message='Enter float.', default=0, ok='OK', cancel='Cancel', title=''):
    while 1:
        s = ask_string(message=message, default=unicode(default), ok=ok, cancel=cancel, title=title)
        if not s:
            return
        try:
            x=int(s)
            return x
        except:
            warning('"%s" is not a valid integer!' % s, title=title)
    
