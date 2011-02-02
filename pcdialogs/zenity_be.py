from wrapcli import call
import tempfile
class Backend():
    def _call(self, args, options, useReturnCode=False, extraargs= []):
        if args.title:
            options["--title"] = args.title
        result = call('zenity', extraargs, options, useReturnCode=useReturnCode)
        if result == '' :
            result = None
        return result
        
    def _message(self, args, kw):
        options = {}
        options["--%s"  % kw] =  None
        options["--text" ] =  args.message
        return self._call(args, options)

    def text(self, args):
        options = {}
        f = tempfile.NamedTemporaryFile()
        f.write(args.text)
        f.flush()
        options["--text-info"] =  None
        options["--filename" ] =  f.name
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
        options["--entry" ] =  None
        options["--text" ] =  args.message
        if pw:
            options["--hide-text" ] =  None
        if args.default:
            options["--entry-text" ] =  args.default 
        return self._call(args, options)
        
    def askString(self, args):
        return self._entry(args, pw=0)
        
    def askPassword(self, args):
        return self._entry(args, pw=1)

    def _file(self, args, multi):
        options = {}
        separator = '|'
        options["--file-selection" ] =  None
        options["--text" ] =  args.message
        if multi:
            options["--multiple" ] =  None
            options["--separator" ] =  separator
        if args.default:
            options["--filename" ] =  args.default 
        result = self._call(args, options)
        if result and multi:
            result = result.split(separator)
        return result
        
    def _choice(self, args, multi):
        options = {}
        separator = '|'
        options["--list" ] =  None
        options["--text" ] =  args.message
        if multi:
            options["--multiple" ] =  None
            options["--checklist" ] =  None
            options["--separator" ] =  separator

            extraargs = ["--column" , 'Select', "--column" , 'Item']
            for x in args.choices:
                extraargs  += ['FALSE', x] 
        else:
            extraargs =  ["--column" , 'Item'] + args.choices
        result = self._call(args, options, extraargs=extraargs)
        if result and multi:
            result = result.split(separator)
        return result
        

    def askFileForOpen(self, args):
        return self._file(args, multi=0)
    
    def askFileForSave(self, args):
        return self._file(args, multi=0)
        
    def askFilesForOpen(self, args):
        return self._file(args, multi=1)

    def askOkCancel(self, args):
        options = {}
        options["--question" ] =  None
        options["--text" ] =  args.message
        result = self._call(args, options, useReturnCode=1)
        result = not result
        return result
        
    def askDate(self, args):
        options = {}
        options["--calendar" ] =  None
        return self._call(args, options)

    def choice(self, args):
        return self._choice(args, multi=0)
        
    def multiChoice(self, args):
        return self._choice(args, multi=1)

