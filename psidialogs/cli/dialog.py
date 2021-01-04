import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


@entrypoint
def dialog_cli(
    dialogtype,
    title="",
    message="",
    choices="",
    backend="",
    childprocess=False,
    preference=[],
):
    if not backend:
        backend = None
    choices = choices.split(",")

    # args = dict(title=title, message=message, choices=choices.split(","), text=text,)

    # funcs = psidialogs.FUNCTIONS
    # log.debug("functions found:")
    # log.debug(funcs)
    # log.debug("searching for:")
    # log.debug(func)
    # f = None
    # for x in funcs:
    #     if x.__name__ == func:
    #         f = x
    # assert f

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
