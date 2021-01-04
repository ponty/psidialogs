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
    childprocess=False,
    preference=[],
):
    if not backend:
        backend = None

    if len(preference):
        psidialogs.set_backend_preference(preference)

    if backend:
        psidialogs._force_backend(backend)

    result = None
    result = psidialogs.dialog(
        dialogtype,
        choices=choices,
        message=message,
        title=title,
        # backend=backend,
        # preference=preference,
        childprocess=childprocess,
    )
    log.debug("result:%s", result)
    if result:
        print(result)
