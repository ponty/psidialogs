import logging
import multiprocessing

from discogui.mouse import PyMouse

# from discogui.hover import active_rectangles
from hover import active_rectangles
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs

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


def target_func(dialogtype):
    return psidialogs.dialog(dialogtype, choices=["a", "b"])


def check_open(backend, dialogtype):
    with SmartDisplay(visible=VISIBLE) as disp:
        t = multiprocessing.Process(
            target=lambda: psidialogs.dialog(dialogtype, choices=["a", "b"])
        )
        t.start()

        disp.waitgrab(timeout=TIMEOUT)
    t.join()


def check_unix(backend, dialogtype):
    if backend:
        psidialogs.force_backend(backend)
    check_open(backend, dialogtype)
    # if backend == "gmessage":  # active editbox
    #     return
    if dialogtype in ["message", "warning", "error"]:
        expect = set([None])
        check_buttons(backend, dialogtype, expect)
    if dialogtype in ["ask_yes_no", "ask_ok_cancel"]:
        expect = set([True, False])
        check_buttons(backend, dialogtype, expect)
