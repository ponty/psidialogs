import inspect
import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


@entrypoint
def opendialog(backend, func, title="", message="", choices="", text=""):
    # TODO:    BackendLoader().force(backend)

    args = dict(title=title, message=message, choices=choices.split(","), text=text,)

    funcs = psidialogs.FUNCTIONS
    log.debug("functions found:")
    log.debug(funcs)
    log.debug("searching for:")
    log.debug(func)
    f = None
    for x in funcs:
        if x.__name__ == func:
            f = x
    assert f
    argnames, varargs, varkw, defaults = inspect.getargspec(f)

    args = dict([(k, v) for (k, v) in args.items() if k in argnames])
    result = None
    # exec "result = psidialogs.%s(**args)" % (func)
    result = psidialogs.__dict__[func](**args)
    log.debug("result:%s", result)
    print(result)
