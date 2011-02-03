from attribdict import attribdict
from mixins import AllMixin
from path import path
from pcdialogs.plugin_loader import get_plugin, get_all_plugins
import logging

_BACKEND = None


def all_backends():
    return get_all_plugins()

def get_backend():
    return _BACKEND.name

def set_backend(backend_preference=['easygui'], force_backend=None):
    global _BACKEND
    _BACKEND = get_plugin(backend_preference=backend_preference, force_backend=force_backend)
    
def _get_backend():
    if not _BACKEND:
        set_backend()
    return _BACKEND

def opendialog(funcname, argdict):
    for (k, v) in argdict.items():
        if v is None:
            argdict[k] = ''

    logging.debug(funcname)
    logging.debug(argdict)
    d = attribdict(argdict)
    b = _get_backend()
    f = b.__class__.__dict__.get(funcname)
    if not f:
        class Backend(b.__class__, AllMixin):
            pass
        b = Backend()
        f = AllMixin.__dict__.get(funcname)
   
    return f(b,d)
