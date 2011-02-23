"""
CLI for functions
"""

def getVersion(func):
    version= None
    for v in '__version__ VERSION version'.split():
        version = func.func_globals.get(v)
        if version:
            break
    return version

def extractInfo(func, debug=False):
    """
    no action

    """
    import inspect


    if func.__doc__:
        doclist = func.__doc__.strip().splitlines()
    else:
        doclist = []

    doclist = map(lambda x: x.strip(), doclist)

    args, varargs, varkw, defaults = inspect.getargspec(func)
    if not defaults:
        defaults = ()
    delta = len(args) - len(defaults)
    defaults = delta * (None,) + defaults
    ispositional = delta * (True,) + (len(args) - delta) * (False,)

    description = (doclist + [''])[0]
    allshortoptions = ['h']
    version=getVersion(func)
    if version:
        allshortoptions.append('v')
##    if debug:
##        allshortoptions.append('d')
    allarguments = []
    for x , d , p in zip(args, defaults, ispositional):
        x = x.lower()
        help = ''
        option_strings = []
        for line in doclist:
            line=line.strip()
            first_word = (line.split() + [''])[0]
            if first_word==':param':
                line=line.replace(':param', '', 1)
                first_word = (line.split() + [''])[0]
            first_word=first_word.strip(':')
            if  first_word == x:
                help=line.replace(x, '', 1).strip()
        if p:
            option_strings.append( x )
        else:
            firstchar = x[0]
            if firstchar not in allshortoptions:
                option_strings.append( '-' +  firstchar)
                allshortoptions.append( firstchar)
            option_strings.append( '--' +  x.replace('_','-'))
        if d:
            help +=' [default=%(default)s]'
        action="store_true" if d is False else None
        allarguments.append( (option_strings , dict(help=help, default=d, action=action) ) )
    if debug:
        allarguments.append( (['--debug'], dict(help='Set logging level to DEBUG', action='store_true') ) )
##        parser.add_argument(*option_strings, **dict(help=help, default=d, action=action) )
    return (allarguments, description, version)

def main(func, debug=True):
    """
    The main function
    """
    if func.func_globals['__name__'] != '__main__':
        return

    import argparse
    import logging


    (allarguments, description, version) = extractInfo(func, debug)
    parser = argparse.ArgumentParser(description=description, version=version)
    for (a, d) in allarguments:
        parser.add_argument(*a, **d )
    args = parser.parse_args()
    if debug:
        if args.debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug('--------------------------------------------------------------------------')
            logging.debug('starting program')
            logging.debug('parsed command line:' + str(args))
        del args.debug
    func(**(args.__dict__))
