import os
import platform
import subprocess
import sys
import time
from typing import Union, List
from psidialogs.util import platform_is_osx, platform_is_win, platform_is_linux


import pygetwindow as gw
import glob, sys
import logging
import multiprocessing
import os, time
from pathlib import Path
from time import sleep

# from discogui.imgutil import grab_no_blink
from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from PIL import Image, ImageChops
from PIL import ImageGrab


import psidialogs

if platform_is_osx():
    import Quartz


TITLE = "psidialogs"


def empty_dir(dir):
    files = glob.glob(os.path.join(dir, "*"))
    for f in files:
        os.remove(f)



def _getAllWindows(excludeDesktop: bool = True, screenOnly: bool = True):
    # Source: https://stackoverflow.com/questions/53237278/obtain-list-of-all-window-titles-on-macos-from-a-python-script/53985082#53985082
    # This returns a list of window info objects, which is static, so needs to be refreshed and takes some time to the OS to refresh it
    # Besides, since it may not have kCGWindowName value and the kCGWindowNumber can't be accessed from Apple Script, it's useless
    flags = (
        Quartz.kCGWindowListExcludeDesktopElements
        if excludeDesktop
        else 0 | Quartz.kCGWindowListOptionOnScreenOnly
        if screenOnly
        else 0
    )
    return Quartz.CGWindowListCopyWindowInfo(flags, Quartz.kCGNullWindowID)


def getAllWindows3():
    if platform_is_osx():
        return [w for w in _getAllWindows() if w.get(Quartz.kCGWindowIsOnscreen)]

    if platform_is_win():
        return gw.getAllWindows()


def getWindowID(w):
    if platform_is_osx():
        return w[Quartz.kCGWindowNumber]
    if platform_is_win():
        return w._hWnd


def getWindowByID(wid):
    for w in getAllWindows3():
        if getWindowID(w) == wid:
            return w


def getAllWindowsID():
    return set([getWindowID(w) for w in getAllWindows3()])


def getBBox(wnd):
    # logging.warning("*** wnd: %s", wnd)
    if platform_is_osx():

        bounds = wnd[Quartz.kCGWindowBounds]
        x = bounds["X"]
        y = bounds["Y"]
        w = bounds["Width"]
        h = bounds["Height"]
        return (
            x,
            y,
            x + w,
            y + h,
        )
    if platform_is_win():
        x = wnd.left
        y = wnd.top
        w = wnd.width
        h = wnd.height
        # https://stackoverflow.com/questions/34139450/getwindowrect-returns-a-size-including-invisible-borders
        # remove invisible border
        bbox = (
            x + 7 + 1,
            y + 1,
            x + w - 7 - 1,
            y + h - 7 - 1,
        )
        # logging.warning("*** bbox: %s", bbox)
        return bbox


def grab(allid):
    while 1:
        time.sleep(1)
        d = getAllWindowsID().difference(allid)
        if d:
            assert len(d) == 1

            # for start, animations
            time.sleep(5)

            assert d == getAllWindowsID().difference(allid)

            logging.debug("new wnd: %s", d)
            w = getWindowByID(max(d))
            bbox = getBBox(w)
            im = ImageGrab.grab(bbox)
            logging.debug("im: %s", im)
            logging.debug("bbox: %s", bbox)
            return im



def func1(backend, dtype):
    psidialogs.force_backend(backend)
    psidialogs.dialog(
        dtype,
        message="This is the message. (%s,%s) \u20ac" % (backend, dtype),
        choices=["one", "two", "three"],
    )


@entrypoint
def main():
    gendir = (
        Path(__file__).absolute().parent
        / "gen"
        / "screenshots"
        / (platform.system() + platform.release())
    )
    logging.info("gendir: %s", gendir)
    os.makedirs(gendir, exist_ok=True)
    empty_dir(gendir)
    try:
        cwd = os.getcwd()
        for backend in sorted(psidialogs.backends()):
            for dialogtype in psidialogs.dialog_types():
                logging.info("======== dialogtype: %s backend: %s", dialogtype, backend)
                psidialogs.force_backend(backend)
                python = sys.executable
                cmd = [
                    python,
                    "-m",
                    "psidialogs.cli.dialog",
                    "-b",
                    backend,
                    "-d",
                    dialogtype,
                    "--title",
                    TITLE,
                    "--message",
                    "This is the 'message'! (%s,%s) \u20ac" % (backend, dialogtype),
                    "--choices",
                    "1 \u20ac",
                    "--choices",
                    "Two",
                    "--choices",
                    "Three,\"'  ",
                ]
                png = backend + "_" + dialogtype + ".png"
                png = os.path.join(gendir, png)
                allid = getAllWindowsID()
                with EasyProcess(cmd):
                    # time.sleep(3)
                    # wait(im0)
                    img = grab(allid)
                    logging.info("saving %s", png)
                    img.save(png)
            # return  # XXX
    finally:
        os.chdir(cwd)
