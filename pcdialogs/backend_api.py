from attribdict import attribdict
from dottedimport import dottedimport
from mixins import AllMixin
from path import path
from submodules import modules
import logging

_BACKEND = 'easygui'


BACKEND_POSTFIX = '_be'
BACKEND_PATTERN = '*' + BACKEND_POSTFIX

def allbackends():
    backends = modules(path(__file__).parent, pattern=BACKEND_PATTERN)
    backends = [x[:-3] for x in backends]
    return backends

def get_backend():
    return _BACKEND

def set_backend(bname):
    global _BACKEND
    _BACKEND=bname
    
def _get_backend():
    return dottedimport('pcdialogs' + '.' + _BACKEND + BACKEND_POSTFIX)

def opendialog(funcname, argdict):
    for (k, v) in argdict.items():
        if v is None:
            argdict[k] = ''

    logging.debug(funcname)
    logging.debug(argdict)
    d = attribdict(argdict)
    class Backend(_get_backend().Backend, AllMixin):
        pass
    f = eval('Backend().%s' % funcname)

    def func(args):
        return f(args)
    
    return func(d)

def version(funcname, argdict):
    return _getbackend().Backend.version()
