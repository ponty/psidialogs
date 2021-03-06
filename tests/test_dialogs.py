import logging
from threading import Thread

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs

log = logging.getLogger(__name__)

VISIBLE = 0
TIMEOUT = 10


def check_buttons(backend, dialogtype, expect):
    expect = list(expect)
    with SmartDisplay(visible=VISIBLE) as disp:
        t = Thread(target=lambda: psidialogs.dialog(dialogtype, backend=backend))
        t.start()

        # wait for displaying the window
        disp.waitgrab(timeout=TIMEOUT)

        buttons = discover_buttons()

        assert len(buttons) == len(expect)
    t.join()

    with SmartDisplay(visible=VISIBLE) as disp:
        mouse = PyMouse()
        print("buttons: %s" % buttons)
        for v, b in zip(expect, buttons):
            ls = [None]

            def fdlg(ls):
                ls[0] = psidialogs.dialog(dialogtype, backend=backend)

            t = Thread(target=fdlg, args=(ls,))
            t.start()
            disp.waitgrab(timeout=TIMEOUT)
            mouse.click(*b.center)
            t.join()
            result = ls[0]
            log.debug("result=%r", result)
            assert result == v


def check_open(backend, dialogtype):
    with SmartDisplay(visible=VISIBLE) as disp:
        t = Thread(
            target=lambda: psidialogs.dialog(dialogtype, backend=backend, choices=["a", "b"])
        )
        t.start()

        disp.waitgrab(timeout=TIMEOUT)
    t.join()


def check(backend, dialogtype):
    log.info("========= check backend:%s dialogtype:%s =========", backend, dialogtype)
    check_open(backend, dialogtype)
    reverse_order = False

    # if backend == "wxpython" and dialogtype != "message":  # wrong button taborder
    #     return
    if backend in ["zenity", "wxpython"]:
        reverse_order = True
    #     if dialogtype in ["ask_ok_cancel", "ask_yes_no"]:
    #         # tab is not working in xvfb and xephyr
    #         return
    # if backend == "gmessage":  # active editbox
    #     return

    if dialogtype in ["message", "warning", "error"]:
        expect = [None]
        check_buttons(backend, dialogtype, expect)
    if dialogtype in ["ask_yes_no", "ask_ok_cancel"]:
        expect = [True, False]
        if reverse_order:
            expect = reversed(expect)
        check_buttons(backend, dialogtype, expect)


def check_backend(backend):
    # TODO:if not BackendLoader().is_console(backend):
    for dtype in psidialogs.dialog_types():
        check(backend, dtype)
