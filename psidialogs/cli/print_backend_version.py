import logging

from entrypoint2 import entrypoint

from psidialogs.loader import backend_version2

log = logging.getLogger(__name__)


@entrypoint
def main(backend):
    """Print psidialogs back-end version.

    :param backend: back-end (example:pyqt5, tkinter,..)
    """
    backend = backend if backend else None

    try:
        exit(0)
        v = backend_version2(backend)
    except Exception as e:
        log.warning(e)
        v = ""
    print(v)
    exit(0)
