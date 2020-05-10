from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from easyprocess import EasyProcess
from nose.tools import with_setup, eq_
from psidialogs.backendloader import BackendLoader
from pyvirtualdisplay.smartdisplay import SmartDisplay
import psidialogs

VISIBLE = 0
TIMEOUT = 30


def check_buttons(cmd, expect):
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(cmd):
            # wait for displaying the window
            disp.waitgrab(timeout=TIMEOUT)

            buttons = discover_buttons()

            eq_(
                len(buttons),
                len(expect),
                msg="dialog does not have expected buttons %s!=%s" % (buttons, expect),
            )

            mouse = PyMouse()
            print "buttons:", buttons
            for v, b in zip(expect, buttons):
                process = EasyProcess(cmd).start().sleep(1)
                mouse.click(*b.center)
                process.wait(timeout=10)
                assert not process.timeout_happened
                eq_(process.stdout, str(v))
                # dialog does not return expected value


def check_open(backend, func):
    cmd = "python -m psidialogs.examples.demo -b {backend} -f {func}".format(
        backend=backend, func=func
    )
    # exception if nothing is displayed
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(cmd):
            disp.waitgrab(timeout=TIMEOUT)


def check(backend, func):
    check_open(backend, func)

    if backend == "pyqt":  # test not working, buttons are not active
        return
    if backend == "wxpython" and func != "message":  # wrong button taborder
        return
    if backend == "easydialogs":
        if func in ["ask_ok_cancel", "ask_yes_no"]:
            # can not hide button in easydialogs-gtk
            return
    if backend == "zenity":
        if func in ["ask_ok_cancel", "ask_yes_no"]:
            # tab is not working in xvfb and xephyr
            return
    if backend == "gmessage":  # active editbox
        return

    cmd = "python -m psidialogs.examples.opendialog {backend} {func} -m hi".format(
        backend=backend, func=func
    )
    if func == "message":
        expect = [None]
        check_buttons(cmd, expect)
    if func == "ask_yes_no":
        expect = [True, False]
        check_buttons(cmd, expect)
    if func == "ask_ok_cancel":
        expect = [True, False]
        check_buttons(cmd, expect)


s = ""
for x in BackendLoader().all_names:
    for f in psidialogs.FUNCTION_NAMES:
        if not BackendLoader().is_console(x):
            s += """
def test_{backend}_{safefunc}():
    check("{backend}","{func}")
""".format(
                backend=x,
                func=f,
                safefunc=f.replace("error", "err").replace("warning", "warn"),
            )
exec s
