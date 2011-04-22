from entrypoint2 import entrypoint
from psidialogs.backendloader import BackendLoader
import inspect
import logging
import os
import psidialogs
import sys

log = logging.getLogger(__name__)

def testdata():
    f = open(__file__)
    text = f.read()
    f.close()
    return dict(
        message="This is a message! (%s)" % BackendLoader().selected().name,
        choices=["One", "Two", "Three"],
        text='%s' % text,
        )

def dialog(func, title='', **kwargs):
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
    #argnames = psidialogs.argnames(func)
    args = testdata()
    if title:
        args['title'] = title
    args = dict([(k, v) for (k, v) in args.items() if k in argnames])
    result=None
    exec 'result = psidialogs.%s(**args)' % (func)
    #result = psidialogs.__dict__[func](**args)
    #print 'result: ' , result
    log.debug('result:'+str(result))
    if result is not None:
        psidialogs.text('Return value="%s"' % result)
        
def selectfunc(title='', function=None, **kwargs):
    if function:
        dialog(function, title, **kwargs)
    else:
        while 1:
            funcs = psidialogs.FUNCTION_NAMES
            funcs.sort()
            func = psidialogs.choice(funcs, 'Select function!', title=title)
            if not func:    
                break
            dialog(func, title, **kwargs)

def selectbackend(backend=None, title='', **kwargs):
    if backend:
        BackendLoader().force(backend)    
        selectfunc(title, **kwargs)
    else:
        while 1:
            #d = dict([(x.backend, x.name) for x in psidialogs.all_backends()])
            #names=sorted(d.keys()
            names=sorted(BackendLoader().all_names)
            b = psidialogs.choice(names, 'Select backend!', title=title)
            if not b:   
                break
            BackendLoader().force(b)
            try:
                BackendLoader().selected()
            except Exception, detail:
                BackendLoader().force(None)
                psidialogs.text('Exception:\n' + str(detail))
                continue
              
            #psidialogs.set_backend(force_backend=d[b])  
            selectfunc(title, **kwargs)

@entrypoint        
def demo(backend=None, function=None, title=''):
    print os.isatty(sys.stdout.fileno())
    selectbackend(backend=backend, function=function, title=title)    
    
