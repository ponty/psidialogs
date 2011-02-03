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
        message="This is a message! (%s)" % pcdialogs.get_backend(),
        choices=["One", "Two", "Three"],
        text='%s' % text,
        )

def dialog(func, title='', **kwargs):
    funcs = pcdialogs.FUNCTIONS
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
    result=None
    exec 'result = pcdialogs.%s(**args)' % (func)
    #result = pcdialogs.__dict__[func](**args)
    #print 'result: ' , result
    log.debug('result:'+str(result))
    if result is not None:
        pcdialogs.text('Return value="%s"' % result)
        
def selectfunc(title='', function=None, **kwargs):
    if function:
        dialog(function, title, **kwargs)
    else:
        while 1:
            funcs = pcdialogs.FUNCTION_NAMES
            funcs.sort()
            func = pcdialogs.choice(funcs, 'Select function!', title=title)
            if not func:    
                break
            dialog(func, title, **kwargs)

def selectbackend(backend=None, title='', **kwargs):
    if backend:
        pcdialogs.set_backend(force_backend=backend)    
        selectfunc(title, **kwargs)
    else:
        while 1:
            #d = dict([(x.backend, x.name) for x in pcdialogs.all_backends()])
            #names=sorted(d.keys()
            names=sorted([x.name for x in pcdialogs.all_backends()])
            b = pcdialogs.choice(names, 'Select backend!', title=title)
            if not b:   
                break
            pcdialogs.set_backend(force_backend=b)  
            #pcdialogs.set_backend(force_backend=d[b])  
            selectfunc(title, **kwargs)
        
def demo(backend=None, function=None, title=''):
    selectbackend(backend=backend, function=function, title=title)    
    
cli4func.main(demo)
