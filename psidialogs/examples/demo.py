import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)

g_backend = ""


def testdata(title, dialogtype):
    return dict(
        message=u"This is the 'message'! (%s,%s) \u20ac" % (g_backend, dialogtype),
        choices=[u"1 \u20ac", "Two", "Three"],
        # text=u"\u20ac\n%s" % text,
        title=title if title else u"title \u20ac",
    )


def dialog(dialogtype, title="", **kwargs):
    args = testdata(title, dialogtype)
    result = psidialogs.dialog(dialogtype, **args)
    psidialogs.message("Return value=%r" % (result))


def select_dialogtype(title="", dialogtype=None, **kwargs):
    if dialogtype:
        dialog(dialogtype, title, **kwargs)
    else:
        while 1:
            dialogtypes = psidialogs.dialog_types()
            dialogtype = psidialogs.choice(
                dialogtypes, "Select dialog type!", title=title
            )
            if not dialogtype:
                break
            dialog(dialogtype, title, **kwargs)


def select_backend(backend=None, title="", **kwargs):
    global g_backend
    if backend:
        g_backend = backend
        psidialogs.set_backend_preference([backend])
        select_dialogtype(title, **kwargs)
    else:
        while 1:
            names = sorted(psidialogs.backends())

            b = psidialogs.choice(names, "Select backend!", title=title)
            if not b:
                break
            g_backend = b
            psidialogs.set_backend_preference([b])
            select_dialogtype(title, **kwargs)


@entrypoint
def demo(backend=None, dialogtype=None, title=""):
    select_backend(backend=backend, dialogtype=dialogtype, title=title)
