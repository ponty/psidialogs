import sys
from path import path
import logging
#import pyanno
##BACKENDS = 'backends'
_backend = None

from submodules import modules
from dottedimport import dottedimport

BACKEND_POSTFIX = '_be'
BACKEND_PATTERN = '*' + BACKEND_POSTFIX

def allbackends():
    backends=modules(path(__file__).parent, pattern=BACKEND_PATTERN)
    backends=[x[:-3] for x in backends]
    return backends

def setbackend(bname):
    global _backend
    _backend = dottedimport( 'pcdialogs'  + '.' + bname + BACKEND_POSTFIX)
##    _backend = __import__( bname + BACKEND_POSTFIX)

from attribdict import attribdict
from mixins import AllMixin
from reflect import returntype
def opendialog(funcname, argdict):
    for (k,v) in argdict.items():
        if v is None:
            argdict[k] = ''

    logging.debug(funcname)
    logging.debug(argdict)
    d = attribdict(argdict)
    class Backend(_backend.Backend, AllMixin):
        pass
    f = eval( 'Backend().%s' % funcname)

    #@pyanno.returnType(returntype(funcname))
    def func(args):
        return f(args)
    
    return func(d)

def version(funcname, argdict):
    return _backend.Backend.version()
setbackend('easygui')
