import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


def testdata(title, backend, func):
    # f = open(__file__)
    # text = f.read()
    # f.close()
    # text = "long text"

    return dict(
        message=u"This is the 'message'! (%s,%s) \u20ac" % (backend, func),
        choices=[u"1 \u20ac", "Two", "Three"],
        # text=u"\u20ac\n%s" % text,
        title=title if title else u"title \u20ac",
    )


def dialog(backend, func, title="", **kwargs):
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
    args = testdata(title, backend, func)
    result = None

    result = psidialogs.dialog(func, backend=backend, **args)
    # if result is not None:
    psidialogs.message("Return value=%r" % (result))


def selectfunc(backend, title="", function=None, **kwargs):
    if function:
        dialog(backend, function, title, **kwargs)
    else:
        while 1:
            funcs = psidialogs.FUNCTION_NAMES
            func = psidialogs.choice(funcs, "Select function!", title=title)
            if not func:
                break
            dialog(backend, func, title, **kwargs)


def selectbackend(backend=None, title="", **kwargs):
    if backend:
        selectfunc(backend, title, **kwargs)
    else:
        while 1:
            names = sorted(psidialogs.backends())

            b = psidialogs.choice(names, "Select backend!", title=title)
            if not b:
                break
            selectfunc(b, title, **kwargs)


@entrypoint
def demo(backend=None, function=None, title=""):
    selectbackend(backend=backend, function=function, title=title)
