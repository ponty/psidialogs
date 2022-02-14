import logging

import psidialogs
from psidialogs.util import platform_is_osx, platform_is_win

log = logging.getLogger(__name__)


def check_dialog(backend, dialogtype):
    try:
        log.info(
            "========= check backend:%s dialogtype:%s =========", backend, dialogtype
        )

        if backend:
            psidialogs._force_backend(backend)
        if platform_is_osx() or platform_is_win():
            from check_dialog_winmacos import check_winmacos

            check_winmacos(backend, dialogtype)
        else:
            from check_dialog_unix import check_unix

            check_unix(backend, dialogtype)
    finally:
        psidialogs._force_backend(None)
