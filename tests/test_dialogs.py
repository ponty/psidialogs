import logging
from threading import Thread

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs

log = logging.getLogger(__name__)

VISIBLE = 0
TIMEOUT = 10


def check_buttons(backend, func, expect):
    expect = list(expect)
    with SmartDisplay(visible=VISIBLE) as disp:
        t = Thread(target=lambda: psidialogs.dialog(func, backend=backend))
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
                ls[0] = psidialogs.dialog(func, backend=backend)

            t = Thread(target=fdlg, args=(ls,))
            t.start()
            disp.waitgrab(timeout=TIMEOUT)
            mouse.click(*b.center)
            t.join()
            result = ls[0]
            log.debug("result=%r", result)
            assert result == v


def check_open(backend, func):
    with SmartDisplay(visible=VISIBLE) as disp:
        t = Thread(
            target=lambda: psidialogs.dialog(func, backend=backend, choices=["a", "b"])
        )
        t.start()

        disp.waitgrab(timeout=TIMEOUT)
    t.join()


def check(backend, func):
    log.info("========= check backend:%s func:%s =========", backend, func)
    check_open(backend, func)
    reverse_order = False

    # if backend == "wxpython" and func != "message":  # wrong button taborder
    #     return
    if backend in ["zenity", "wxpython"]:
        reverse_order = True
    #     if func in ["ask_ok_cancel", "ask_yes_no"]:
    #         # tab is not working in xvfb and xephyr
    #         return
    # if backend == "gmessage":  # active editbox
    #     return

    if func in ["message", "warning", "error"]:
        expect = [None]
        check_buttons(backend, func, expect)
    if func in ["ask_yes_no", "ask_ok_cancel"]:
        expect = [True, False]
        if reverse_order:
            expect = reversed(expect)
        check_buttons(backend, func, expect)


def check_backend(backend):
    # TODO:if not BackendLoader().is_console(backend):
    for func in psidialogs.FUNCTION_NAMES:
        check(backend, func)
