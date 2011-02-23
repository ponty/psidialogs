from attribdict import attribdict
from mixins import AllMixin
from psidialogs.backendloader import BackendLoader
import logging


def opendialog(funcname, argdict):
    for (k, v) in argdict.items():
        if v is None:
            argdict[k] = ''

    logging.debug(funcname)
    logging.debug(argdict)
    d = attribdict(argdict)
    b = BackendLoader().selected()
    f = b.__class__.__dict__.get(funcname)
    if not f:
        class Backend(b.__class__, AllMixin):
            pass
        b = Backend()
        f = AllMixin.__dict__.get(funcname)
   
    return f(b,d)
