import logging
import multiprocessing

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs

log = logging.getLogger(__name__)

VISIBLE = 0
TIMEOUT = 10


def check_buttons(dialogtype, expect):
    expect = list(expect)
    with SmartDisplay(visible=VISIBLE) as disp:
        t = multiprocessing.Process(target=lambda: psidialogs.dialog(dialogtype))
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
            q = multiprocessing.Queue()

            def fdlg(q):
                ret = psidialogs.dialog(dialogtype)
                q.put(ret)

            t = multiprocessing.Process(target=fdlg, args=(q,))
            t.start()
            disp.waitgrab(timeout=TIMEOUT)
            mouse.click(*b.center)
            result = q.get()
            t.join()
            log.debug("result=%r", result)
            assert result == v


def check_open(backend, dialogtype):
    with SmartDisplay(visible=VISIBLE) as disp:
        t = multiprocessing.Process(
            target=lambda: psidialogs.dialog(dialogtype, choices=["a", "b"])
        )
        t.start()

        disp.waitgrab(timeout=TIMEOUT)
    t.join()


def check(backend, dialogtype):
    try:
        log.info(
            "========= check backend:%s dialogtype:%s =========", backend, dialogtype
        )
        if backend:
            psidialogs._force_backend(backend)
        check_open(backend, dialogtype)
        reverse_order = False

        # if backend == "wxpython" and dialogtype != "message":  # wrong button taborder
        #     return

        if backend in ["zenity", "wxpython", "pyside2", "pyqt5"]:
            reverse_order = True

        #     if dialogtype in ["ask_ok_cancel", "ask_yes_no"]:
        #         # tab is not working in xvfb and xephyr
        #         return
        # if backend == "gmessage":  # active editbox
        #     return

        if dialogtype in ["message", "warning", "error"]:
            expect = [None]
            check_buttons(dialogtype, expect)
        if dialogtype in ["ask_yes_no", "ask_ok_cancel"]:
            expect = [True, False]
            if reverse_order:
                expect = reversed(expect)
            check_buttons(dialogtype, expect)
    finally:
        psidialogs._force_backend(None)


# def check_backend(backend):
#     # TODO:if not BackendLoader().is_console(backend):
#     for dtype in psidialogs.dialog_types():
#         check(backend, dtype)
