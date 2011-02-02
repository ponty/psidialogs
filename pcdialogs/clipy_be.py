
class Backend():
    console=True
    def message(self, args):
        print args.message
    def ask_string(self, args):
        return raw_input(args.message)
        
