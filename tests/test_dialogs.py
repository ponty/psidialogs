import logging
import sys

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs

log = logging.getLogger(__name__)

VISIBLE = 0
TIMEOUT = 15


def check_buttons(cmd, expect):
    expect = list(expect)
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(cmd) as proc:
            # def imgcheck(im):
            #     log.info(im)
            #     im = disp.autocrop(im)
            #     log.info(im)
            #     if not proc.is_alive():
            #         raise ValueError('Process crashed.')
            #     if im:
            #         return True

            # wait for displaying the window
            disp.waitgrab(timeout=TIMEOUT)
            # disp.waitgrab(timeout=TIMEOUT, autocrop=False,cb_imgcheck=imgcheck)

            buttons = discover_buttons()

            assert len(buttons) == len(expect)
            # msg="dialog does not have expected buttons %s!=%s" % (buttons, expect),

            mouse = PyMouse()
            print("buttons: %s" % buttons)
            for v, b in zip(expect, buttons):
                # process = EasyProcess(cmd).start().sleep(1)
                with EasyProcess(cmd) as process:
                    process.sleep(1)
                    mouse.click(*b.center)
                    process.wait(timeout=10)
                    assert not process.timeout_happened
                    assert process.stdout == str(v)
                    # dialog does not return expected value


def check_open(backend, func):
    cmd = [
        sys.executable,
        "-m",
        "psidialogs.cli.demo",
        "-b",
        backend,
        "-f",
        func,
        "--debug",
    ]
    # exception if nothing is displayed
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(cmd) as proc:
            # def imgcheck(im):
            #     log.info(im)
            #     im = disp.autocrop(im)
            #     log.info(im)
            #     if not proc.is_alive():
            #         raise ValueError('Process crashed.')
            #     if im:
            #         return True
            #     return False
            # disp.waitgrab(timeout=TIMEOUT, autocrop=False,cb_imgcheck=imgcheck)
            disp.waitgrab(timeout=TIMEOUT)


def check(backend, func):
    log.info("========= check backend:%s func:%s =========", backend, func)
    check_open(backend, func)
    return  # TODO

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

    cmd = [
        sys.executable,
        "-m",
        "psidialogs.examples.opendialog",
        backend,
        func,
        "-m",
        "hi",
    ]
    if func in ["message", "warning", "error"]:
        expect = [None]
        check_buttons(cmd, expect)
    if func in ["ask_yes_no", "ask_ok_cancel"]:
        expect = [True, False]
        if reverse_order:
            expect = reversed(expect)
        check_buttons(cmd, expect)
    # if func == "ask_ok_cancel":
    #     expect = [True, False]
    #     check_buttons(cmd, expect)


def check_backend(backend):
    # TODO:if not BackendLoader().is_console(backend):
    for func in psidialogs.FUNCTION_NAMES:
        check(backend, func)
