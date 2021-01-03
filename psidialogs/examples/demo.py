import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


def testdata(title, backend, dialogtype):
    # f = open(__file__)
    # text = f.read()
    # f.close()
    # text = "long text"

    return dict(
        message=u"This is the 'message'! (%s,%s) \u20ac" % (backend, dialogtype),
        choices=[u"1 \u20ac", "Two", "Three"],
        # text=u"\u20ac\n%s" % text,
        title=title if title else u"title \u20ac",
    )


def dialog(backend, dialogtype, title="", **kwargs):
    args = testdata(title, backend, dialogtype)
    result = psidialogs.dialog(dialogtype, backend=backend, **args)
    psidialogs.message("Return value=%r" % (result))


def select_dialogtype(backend, title="", dialogtype=None, **kwargs):
    if dialogtype:
        dialog(backend, dialogtype, title, **kwargs)
    else:
        while 1:
            dialogtypes = psidialogs.dialog_types()
            dialogtype = psidialogs.choice(dialogtypes, "Select dialog type!", title=title)
            if not dialogtype:
                break
            dialog(backend, dialogtype, title, **kwargs)


def select_backend(backend=None, title="", **kwargs):
    if backend:
        select_dialogtype(backend, title, **kwargs)
    else:
        while 1:
            names = sorted(psidialogs.backends())

            b = psidialogs.choice(names, "Select backend!", title=title)
            if not b:
                break
            select_dialogtype(b, title, **kwargs)


@entrypoint
def demo(backend=None, dialogtype=None, title=""):
    select_backend(backend=backend, dialogtype=dialogtype, title=title)
