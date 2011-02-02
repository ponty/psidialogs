import pcdialogs 
from pcdialogs import cli4func
import logging

def testdata():
    f = open(__file__)
    text = f.read()
    f.close()
    return dict(
        message="Test message",
        choices=["One", "Two", "Three"],
        text = '%s' % text,
        )

def dialog(func, title='', **kwargs):
    argnames = pcdialogs.argnames(func)
    args = testdata()
    if title:
        args['title'] =title
    args = dict([(k,v) for (k,v) in args.items() if k in argnames])
    exec 'result = pcdialogs.%s(**args)' % (func )
    print 'result: ' , result
    
def selectfunc(title='', function=None, **kwargs):
    if function:
        dialog(function, title, **kwargs)
    else:
        while 1:
            funcs = pcdialogs.functions()
            funcs.sort()
            func = pcdialogs.choice(funcs, 'Select function!', title=title)
            if not func:    
                break
            dialog(func, title, **kwargs)

def selectbackend(backend=None, title='', **kwargs):
    if backend:
        pcdialogs.setbackend(backend)    
        selectfunc(title, **kwargs)
    else:
        while 1:
            b = pcdialogs.choice(pcdialogs.allbackends(), 'Select backend!', title=title)
            if not b:   
                break
            pcdialogs.setbackend(b)  
            selectfunc(title, **kwargs)
        
def demo(backend=None, function=None, title=''):
    selectbackend(backend=backend, function=function, title=title)    
    
cli4func.main(demo)
