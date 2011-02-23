from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin
import tempfile

EasyProcess('zenity --version').check()

class Backend(IPlugin):
    backend='Zenity'
    #backend_version = BACKEND_VERSION
    
    def __init__(self):
        pass
    
    def _call(self, args, options, useReturnCode=False, extraargs=[]):
        if args.title:
            options["--title"] = args.title
        def dict2list(d):
            ls=[]
            for k,v in d.items():
                if k:
                    ls+=[k]
                if v:
                    ls+=[v]
            return ls
        #print ['zenity']  , dict2list(options) , extraargs
        cmd = ['zenity']  + dict2list(options) + extraargs
        p = EasyProcess(cmd).call()
        if useReturnCode:
            return p.return_code
        result = p.stdout.strip()
        if not result:
            result = None
        return result
        
    def _message(self, args, kw):
        options = {}
        options["--%s" % kw] = None
        options["--text" ] = args.message
        return self._call(args, options)

    def text(self, args):
        options = {}
        f = tempfile.NamedTemporaryFile()
        f.write(args.text)
        f.flush()
        options["--text-info"] = None
        options["--filename" ] = f.name
        result = self._call(args, options)
        f.close()
        return result
        
    def message(self, args):
        return self._message(args, 'info')
        
    def warning(self, args):
        return self._message(args, 'warning')
        
    def error(self, args):
        return self._message(args, 'error')
    
    def _entry(self, args, pw):
        options = {}
        options["--entry" ] = None
        options["--text" ] = args.message
        if pw:
            options["--hide-text" ] = None
        if args.default:
            options["--entry-text" ] = args.default 
        return self._call(args, options)
        
    def ask_string(self, args):
        return self._entry(args, pw=0)
        
    def _file(self, args, multi):
        options = {}
        separator = '|'
        options["--file-selection" ] = None
        options["--text" ] = args.message
        if multi:
            options["--multiple" ] = None
            options["--separator" ] = separator
        if args.default:
            options["--filename" ] = args.default 
        result = self._call(args, options)
        if result and multi:
            result = result.split(separator)
        return result
        
    def _choice(self, args, multi):
        options = {}
        separator = '|'
        options["--list" ] = None
        options["--text" ] = args.message
        if multi:
            options["--multiple" ] = None
            options["--checklist" ] = None
            options["--separator" ] = separator

            extraargs = ["--column" , 'Select', "--column" , 'Item']
            for x in args.choices:
                extraargs += ['FALSE', x] 
        else:
            extraargs = ["--column" , 'Item'] + args.choices
        result = self._call(args, options, extraargs=extraargs)
        if result and multi:
            result = result.split(separator)
        return result
        

    def ask_file(self, args):
        return self._file(args, multi=0)
    
    def _ask_question(self, args, ok, cancel):
        options = {}
        options["--question" ] = None
        options["--text" ] = args.message
        options["--ok-label" ] = ok
        options["--cancel-label" ] = cancel
        result = self._call(args, options, useReturnCode=1)
        result = not result
        return result
    
    def ask_ok_cancel(self, args):
        return self._ask_question(args, ok='OK', cancel='Cancel')
        
    def ask_yes_no(self, args):
        return self._ask_question(args, ok='Yes', cancel='No')

    def choice(self, args):
        return self._choice(args, multi=0)
        
    def multi_choice(self, args):
        return self._choice(args, multi=1)

