import logging
import multiprocessing
import time

import psidialogs


log = logging.getLogger(__name__)


def target_func(backend, dialogtype):
    if backend:
        psidialogs.force_backend(backend)
    return psidialogs.dialog(
        dialogtype, message=backend, title=backend, choices=["a", "b"]
    )


def check_open_novirt(backend, dialogtype):
    t = multiprocessing.Process(
        target=target_func,
        args=(
            backend,
            dialogtype,
        )
    )
    t.start()
    time.sleep(3)

    # d = Path(__file__).absolute().parent / "testout"
    # os.makedirs(d, exist_ok=True)
    # im = grab()
    # im.save(d / f"{backend}_{dialogtype}.png")

    assert t.is_alive()
    t.terminate()
    # t.join()


def check_winmacos(backend, dialogtype):
    check_open_novirt(backend, dialogtype)
