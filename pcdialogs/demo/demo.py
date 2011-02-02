from pcdialogs import cli4func
import inspect
import logging
import pcdialogs

log = logging.getLogger(__name__)

def testdata():
    f = open(__file__)
    text = f.read()
    f.close()
    return dict(
        message="Backend is "+pcdialogs.get_backend(),
        choices=["One", "Two", "Three"],
        text='%s' % text,
        )

def dialog(func, title='', **kwargs):
    funcs = pcdialogs.functions
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
    #argnames = pcdialogs.argnames(func)
    args = testdata()
    if title:
        args['title'] = title
    args = dict([(k, v) for (k, v) in args.items() if k in argnames])
    exec 'result = pcdialogs.%s(**args)' % (func)
    print 'result: ' , result
    
def selectfunc(title='', function=None, **kwargs):
    if function:
        dialog(function, title, **kwargs)
    else:
        while 1:
            funcs = pcdialogs.function_names
            funcs.sort()
            func = pcdialogs.choice(funcs, 'Select function!', title=title)
            if not func:    
                break
            dialog(func, title, **kwargs)

def selectbackend(backend=None, title='', **kwargs):
    if backend:
        pcdialogs.set_backend(backend)    
        selectfunc(title, **kwargs)
    else:
        while 1:
            b = pcdialogs.choice(pcdialogs.allbackends(), 'Select backend!', title=title)
            if not b:   
                break
            pcdialogs.set_backend(b)  
            selectfunc(title, **kwargs)
        
def demo(backend=None, function=None, title=''):
    selectbackend(backend=backend, function=function, title=title)    
    
cli4func.main(demo)
