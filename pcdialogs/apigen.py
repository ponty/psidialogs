import cog
import inspect
from dottedimport import dottedimport
import interfacemap
from attribdict import attribdict
from pprint import pformat
def commonApiFunctionList():
##    code = ', '.join( [  '"%s"' % f for f, args in interfacemap.commonApiFunctions() ] )
##    code = dict(interfacemap.commonApiFunctions()).__repr__()
    code = pformat(dict(interfacemap.commonApiFunctions()))
    code = '_dict=' + code
    cog.outl( code );
        
def generateCommonAPI(funcname):
    for fin, (argsin,typ, defaults) in interfacemap.commonApiFunctions():
        vars = attribdict()    

        vars.fin = fin
        vars.fout = funcname
        vars.doc =  'generated function'
        vars.argspecin = ', '.join( map(lambda (a,d): '%s=%s' %(a,d), zip(argsin, defaults) ) )
        dictout = ', '.join( map(lambda x: '%s=%s' %(x, x), argsin) )
        vars.argspecout = '"%s" , dict(%s)' % (fin, dictout )
        _mapinterface(vars)

def moduleFunctions(modname):
    mod = dottedimport(modname)
    allfunc = mod.__dict__.values()
    allfunc = filter( inspect.isfunction , allfunc)
    if hasattr(mod, '__all__'):
        allfunc = filter( lambda f: f.__name__ in mod.__all__, allfunc)
    return allfunc
    
def generateApi(refname, modname, decorator=None):
##    if not refname:
##        refname = modname
        
    allfunc = moduleFunctions(modname)
    apiMap=  interfacemap.MapCommonApi2SelectedApi(refname)
    for func in allfunc:
        (args, varargs, varkw, defaults) = inspect.getargspec( func)
##        assert not varargs or not len(varargs)
##        assert not varkw or not len(varkw.keys())

        vars = attribdict()    

        (f, argmap) = apiMap.func(func.__name__ )
##        print f,argmap
        vars.doc =  'Original doc: ' + str(func.__doc__ )
        if argmap is not None and f is not None :
            vars.fin =  func.__name__ 
            vars.fout = f
            vars.fout = 'common_api.' + vars.fout
            vars.argspecin = inspect.formatargspec( args, varargs, varkw, defaults)[1:-1]
            args = filter(argmap.has_key, args) 
            vars.argspecout = ', '.join( map(lambda x: '%s=%s' %(argmap[x], x), args) )
            _mapinterface(vars, classmethod=0,decorator=decorator)

def generateBackend(refname, callname,  decorator=None):
    modname = callname
##    if not refname:
##        refname = modname
        
##    allfunc = moduleFunctions(modname)
    apiMap=  interfacemap.MapCommonApi2SelectedApi(refname, inverse=1)
##    print apiMap
    allfunc = apiMap.allfunc()
    for func in allfunc:
##        (args, varargs, varkw, defaults) = inspect.getargspec( func)
##        assert not varargs or not len(varargs)
##        assert not varkw or not len(varkw.keys())

        vars = attribdict()    

##        print func
        (f, argmap) = apiMap.func(func)
##        print f,argmap
        vars.doc =  'generated function'
        if argmap is not None and f is not None :
            vars.fout =  '%s.%s' % ( modname , f)
            vars.fin = func
##            vars.argspecin = 'self, args, extra = {}' 
            vars.argspecin = 'self, args' 
##                args = filter(argmap.has_key, args) 
            vars.argspecout = ', '.join( map(lambda x: '%s=args.%s' %(argmap[x], x), argmap.keys()) )
##            vars.argspecout = '**filterNone(%s, **extra)' % vars.argspecout
            vars.argspecout = '%s' % vars.argspecout
##            vars.argspecout = '**filterNone(%s)' % vars.argspecout
            _mapinterface(vars, classmethod=1,decorator=decorator)

def _mapinterface(vars, classmethod=False, decorator=None):
    code = '''
def %(fin)s(%(argspecin)s):
    """%(doc)s"""
    return %(fout)s(%(argspecout)s)'''  % vars
    
    if decorator    :
        code = '\n@' + decorator + code 
##    print code
    if classmethod:
        code = ''.join( map(lambda x: '    '+x , code.splitlines(1)))
        code = '## for cog indent\n' + code + '\n'
    cog.out( code , dedent=0, trimblanklines=1);


