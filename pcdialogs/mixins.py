from itertools import count

class AllMixin:
    def multi_choice(self, args):
        r = self.choice(args)
        if r:
            r = [r]
        else:
            r = None
        return r
        
    def ask_files(self, args):
        args = args.copy()
        args.save=False
        r = self.ask_file(args)
        if r:
            r = [r]
        else:
            r = None
        return r
        
    def text(self, args):
        args = args.copy()
        args.message = args.message + '\n' + args.text 
        args.text = None
        return self.message(args)
        
    def choice(self, args):
        args = args.copy()
        lines = [ '[%s] %s' % x  for x in zip(count(), args.choices) ]
        args.message += '\n' + '\n'.join(lines) 
        args.message += '\nSelect:'
        args.min = None
        args.max = None
##        self.text(args)
        i = self.ask_string(args)
        if not i:
            return None
        i = int(i)
        if i >= 0 and i < len(args.choices):
            return args.choices[i]
        else:
            return None

    def error(self, args):
        return self.warning(args)

    def warning(self, args):
        return self.message(args)

    def ask_file(self, args):
        return self.ask_string(args)

    def ask_folder(self, args):
        return self.ask_string(args)

    def button_choice(self, args):
        result = self.choice(args)
        if result is None:
            result = args.choices[0]
        return result

    def _yesno(self, args, choices):
        args.choices = choices
        result = self.button_choice(args)
        return result != choices[1]
        
    def ask_ok_cancel(self, args):
        return self._yesno(args, ['OK', 'Cancel'])

    def ask_yes_no(self, args):
        return self._yesno(args, ['Yes', 'No'])

