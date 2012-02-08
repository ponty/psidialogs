from entrypoint2 import entrypoint
from psidialogs.backendloader import BackendLoader
import inspect
import logging
import psidialogs

log = logging.getLogger(__name__)

OMEGA =u'\u03A9'

def dialog(func):
    title = choices = text = message = unicode(u'unicode test, omega='+OMEGA)
    args = dict(
              title=title,
              message=message,
              choices=choices.split(','),
              text=text,
              )
    
    funcs = psidialogs.FUNCTIONS
    log.debug('functions found:')
    log.debug(funcs)
    log.debug('searching for:')
    log.debug(func)
    f = None
    for x in funcs:
        if x.__name__ == func:
            f = x
    assert f
    argnames, varargs, varkw, defaults = inspect.getargspec(f)

    args = dict([(k, v) for (k, v) in args.items() if k in argnames])
    result = None
    exec 'result = psidialogs.%s(**args)' % (func)
    print result
        
        
    
def selectfunc(function=None, **kwargs):
    if not function:
        funcs = psidialogs.FUNCTION_NAMES
        funcs.sort()
        function = psidialogs.choice(funcs, 'Select function!')
    dialog(function, **kwargs)

def selectbackend(backend=None, **kwargs):
    if not  backend:
        names=sorted(BackendLoader().all_names)
        backend = psidialogs.choice(names, 'Select backend!')
    BackendLoader().force(backend)    
    selectfunc(**kwargs)
          
            
@entrypoint        
def unicode_demo(backend='pygtk', function='message', string_type='unicode'):
#    print os.isatty(sys.stdout.fileno())
    selectbackend(backend=backend, function=function)    
