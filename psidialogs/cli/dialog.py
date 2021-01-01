import logging

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)


@entrypoint
def dialog_cli(func, title="", message="", choices="", text="", backend=""):
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

    result = None
    result = psidialogs.dialog(
        func, choices=choices, message=message, title=title, backend=backend
    )
    log.debug("result:%s", result)
    print(result)
