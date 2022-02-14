import logging
import multiprocessing
import os
import time

# from discogui.hover import active_rectangles
from pathlib import Path

from PIL.ImageGrab import grab

import psidialogs

log = logging.getLogger(__name__)


def target_func(dialogtype):
    return psidialogs.dialog(dialogtype, choices=["a", "b"])


def check_open_novirt(backend, dialogtype):
    t = multiprocessing.Process(
        target=target_func,
        args=(dialogtype,)
        # lambda: psidialogs.dialog(dialogtype, choices=["a", "b"])
    )
    t.start()
    time.sleep(3)

    d = Path(__file__).absolute().parent / "testout"
    os.makedirs(d, exist_ok=True)
    im = grab()
    im.save(d / f"{backend}_{dialogtype}.png")

    assert t.is_alive()
    t.terminate()
    # t.join()


def check_winmacos(backend, dialogtype):
    check_open_novirt(backend, dialogtype)
