import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


@entrypoint
def dialog_cli(
    dialogtype="message",
    title="",
    message="",
    choices=[],
    backend="",
    preference=[],
):
    psidialogs._ENABLE_CHILDPROCESS = False
    if not backend:
        backend = None

    if not title:
        title = "psidialogs"

    if len(preference):
        psidialogs.set_backend_preference(preference)

    if backend:
        psidialogs.force_backend(backend)

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
