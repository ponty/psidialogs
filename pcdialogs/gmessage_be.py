from wrapcli import call
from itertools import count

class Backend():
    def _call(self, args, options, useReturnCode=0):
        if args.title:
            options["-name"] = args.title
        options['-center'] = None
        return call('gmessage', [args.message], options, useReturnCode=useReturnCode)
        
    def message(self, args):
        options = {}
        options['-buttons'] = 'GTK_STOCK_OK:0'
        options['-default'] = 'GTK_STOCK_OK'
        return self._call(args, options)
        
    def _question(self, buttons, args):
        options = {}
        options['-buttons'] = buttons
        options['-default'] = buttons.split(',')[not bool(args.default)]
        return self._call(args, options, useReturnCode=1)
    def askOkCancel(self, args):
        return bool(self._question('GTK_STOCK_OK:1,GTK_STOCK_CANCEL:0', args))
    def askYesNo(self, args):
        return bool(self._question('GTK_STOCK_YES:1,GTK_STOCK_NO:0', args))
    def buttonChoice(self, args):
        buttons = ','.join( [ '_%s:%d' % (x,i) for x,i in zip(args.choices, count()) ])
        result = self._question(buttons, args)
        return args.choices[result]
        
    def askString(self, args):
        options = {}
##        options['-buttons'] = 'GTK_STOCK_OK:1,GTK_STOCK_CANCEL:0'
##        options['-default'] = 'GTK_STOCK_OK'
        if args.default:
            options["-entrytext" ] =  args.default 
        else:
            options["-entry" ] =  None
        return self._call(args, options)
        

