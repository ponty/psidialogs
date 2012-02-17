

def uniencode(s):
    if isinstance(s, unicode):
        s = s.encode('utf-8')      
    return s  

def unidecode(s):
    if isinstance(s, str):
        s = s.decode('utf-8')      
    return s  

def ansi_dialog(func):
    def wrapper(self, args):
        if 'choices' in args:
            args.choices = map(uniencode, args.choices)
        if 'message' in args:
            args.message = uniencode(args.message)
        if 'title' in args:
            args.title = uniencode(args.title)
        if 'text' in args:
            args.text = uniencode(args.text)
        result = func(self, args)
        if isinstance(result, str):
            result = unidecode(result)
        if isinstance(result, list):
            result = map(unidecode, result)
        return result
    return wrapper
