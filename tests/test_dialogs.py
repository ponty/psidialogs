import logging
import multiprocessing

from discogui.hover import active_rectangles
from discogui.mouse import PyMouse
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs
from psidialogs.util import platform_is_osx, platform_is_win

log = logging.getLogger(__name__)

VISIBLE = 0
TIMEOUT = 300


def check_buttons(backend, dialogtype, expect):
    with SmartDisplay(visible=VISIBLE) as disp:
        t = multiprocessing.Process(target=lambda: psidialogs.dialog(dialogtype))
        t.start()

        # wait for displaying the window
        disp.waitgrab(timeout=TIMEOUT)

        # buttons = discover_buttons()
        if backend in ["pyside2", "pyqt5"]:
            _ = active_rectangles()  # warm up for qt
        buttons = active_rectangles()

        assert len(buttons) == len(expect)
    t.join()

    with SmartDisplay(visible=VISIBLE) as disp:
        mouse = PyMouse()
        print("buttons: %s" % buttons)
        result_set = set()
        for b in buttons:
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
            result_set.add(result)
        assert result_set == set(expect)


def check_open_novirt(backend, dialogtype):
    t = multiprocessing.Process(
        target=lambda: psidialogs.dialog(dialogtype, choices=["a", "b"])
    )
    t.start()
    time.sleep(3)
    assert t.is_alive()
    t.terminate()
    # t.join()


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
        if platform_is_osx() or platform_is_win():
            check_open_novirt(backend, dialogtype)
        else:
            check_open(backend, dialogtype)
            # if backend in ["zenity", "wxpython", "pyside2", "pyqt5"]:
            #    reverse_order = True
            # if backend == "gmessage":  # active editbox
            #     return
            if dialogtype in ["message", "warning", "error"]:
                expect = set([None])
                check_buttons(backend, dialogtype, expect)
            if dialogtype in ["ask_yes_no", "ask_ok_cancel"]:
                expect = set([True, False])
                # if reverse_order:
                #     expect = reversed(expect)
                check_buttons(backend, dialogtype, expect)
    finally:
        psidialogs._force_backend(None)


# def check_backend(backend):
#     # TODO:if not BackendLoader().is_console(backend):
#     for dtype in psidialogs.dialog_types():
#         check(backend, dtype)
