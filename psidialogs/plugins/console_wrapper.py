from psidialogs.unicodeutil import uniencode, unidecode
from yapsy.IPlugin import IPlugin

class Backend(IPlugin):
    console = True
    backend = 'console'
    #backend_version
    
    def message(self, args):
        msg = args.message + '[ENTER]'
        msg = uniencode(msg)
        raw_input(msg)
        
    def ask_string(self, args):
        answer = raw_input(uniencode(args.message))
        return unidecode(answer)
    
    def ask_yes_no(self, args):
        msg = args.message
        msg = uniencode(msg)
        msg += ' [Yes/No] '
        answers_yes = 'yes y'.split()
        answers_no = 'no n'.split()
        answers = answers_yes + answers_no
        s = ''
        while 1:
            s = raw_input(msg)
            s = unidecode(s)
            s = s.lower().strip()
            if s in answers:
                break
            
        b = s in answers_yes
        
        return b
    
    def ask_ok_cancel(self, args):
        return self.ask_yes_no(args)
    
    def warning(self, args):
        args.message = '[WARNING] ' + args.message
        return self.message(args)

    def error(self, args):
        args.message = '[ERROR] ' + args.message
        return self.message(args)
