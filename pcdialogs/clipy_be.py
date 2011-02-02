
class Backend():
    def message(self, args):
        print args.message
    def askString(self, args):
        return raw_input(args.message)
        
