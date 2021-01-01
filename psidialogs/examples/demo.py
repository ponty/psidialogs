import inspect
import logging

from entrypoint2 import entrypoint

import psidialogs
from psidialogs.backendloader import BackendLoader

log = logging.getLogger(__name__)


def testdata(title, func):
    # f = open(__file__)
    # text = f.read()
    # f.close()
    # text = "long text"

    return dict(
        message=u"This is the 'message'! (%s,%s) \u20ac"
        % (BackendLoader().selected().name, func),
        choices=[u"1 \u20ac", "Two", "Three"],
        # text=u"\u20ac\n%s" % text,
        title=title if title else u"title \u20ac",
    )


def dialog(func, title="", **kwargs):
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
    # argnames = psidialogs.argnames(func)
    args = testdata(title, func)
    args = dict([(k, v) for (k, v) in args.items() if k in argnames])
    result = None
    # exec "result = psidialogs.%s(**args)" % (func)
    result = psidialogs.__dict__[func](**args)
    if result is not None:
        psidialogs.message("Return value=%s (%r)" % (result, result))


def selectfunc(title="", function=None, **kwargs):
    if function:
        dialog(function, title, **kwargs)
    else:
        while 1:
            funcs = psidialogs.FUNCTION_NAMES
            # funcs.sort()
            func = psidialogs.choice(funcs, "Select function!", title=title)
            if not func:
                break
            dialog(func, title, **kwargs)


def selectbackend(backend=None, title="", **kwargs):
    if backend:
        BackendLoader().force(backend)
        selectfunc(title, **kwargs)
    else:
        while 1:
            # d = dict([(x.backend, x.name) for x in psidialogs.all_backends()])
            # names=sorted(d.keys()
            names = sorted(BackendLoader().all_names)
            b = psidialogs.choice(names, "Select backend!", title=title)
            if not b:
                break
            BackendLoader().force(b)
            try:
                BackendLoader().selected()
            except Exception as detail:
                BackendLoader().force(None)
                psidialogs.message("Exception:\n%s" % detail)
                continue

            # psidialogs.set_backend(force_backend=d[b])
            selectfunc(title, **kwargs)


@entrypoint
def demo(backend=None, function=None, title=""):
    # print(os.isatty(sys.stdout.fileno()))
    selectbackend(backend=backend, function=function, title=title)
