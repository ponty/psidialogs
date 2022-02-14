import logging
import multiprocessing

import psidialogs

# from discogui.hover import active_rectangles


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
    assert t.is_alive()
    t.terminate()
    # t.join()


def check_winmacos(backend, dialogtype):
    check_open_novirt(backend, dialogtype)
