from yapsy.IPlugin import IPlugin

class Backend(IPlugin):
    console = True
    backend = 'console'
    #backend_version
    
    def message(self, args):
        print raw_input(args.message)
        
    def ask_string(self, args):
        return raw_input(args.message)
        
    def ask_yes_no(self, args):
        msg = args.message
        msg += ' [Yes/No] '
        answers_yes = 'yes y'.split()
        answers_no = 'no n'.split()
        answers = answers_yes + answers_no
        s = ''
        while 1:
            s = raw_input(msg)
            s = s.lower().strip()
            if s in answers:
                break
            
        b = s in answers_yes
        
        return b
    
    def ask_ok_cancel(self, args):
        return self.ask_yes_no(args)
    
    def warning(self, args):
        args.message='[WARNING] '+args.message
        return self.message(args)

    def error(self, args):
        args.message='[ERROR] '+args.message
        return self.message(args)
