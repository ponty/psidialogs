import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


@entrypoint
def dialog_cli(
    dialogtype,
    title="",
    message="",
    choices=[],
    backend="",
    preference=[],
):
    psidialogs._ENABLE_CHILDPROCESS = False
    if not backend:
        backend = None

    if len(preference):
        psidialogs.set_backend_preference(preference)

    if backend:
        psidialogs.set_backend_preference([backend], disable_others=True)

    result = None
    result = psidialogs.dialog(
        dialogtype,
        choices=choices,
        message=message,
        title=title,
    )
    log.debug("result:%s", result)
    if result:
        print(result)
