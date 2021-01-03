import logging

from psidialogs.err import FailedBackendError
from psidialogs.util import run_mod_as_subproc

log = logging.getLogger(__name__)


def childprocess_backend_version(backend):
    p = run_mod_as_subproc("psidialogs.cli.print_backend_version", [backend])
    if p.return_code != 0:
        log.warning(p)
        raise FailedBackendError(p)

    return p.stdout


def childprocess_dialog(dialogtype, argdict, backend=None):
    title = argdict["title"]
    message = argdict["message"]
    choices = argdict["choices"]

    # with TemporaryDirectory(prefix="psidialogs") as tmpdirname:
    # filename = os.path.join(tmpdirname, "screenshot.png")
    # cmd = ["--filename", filename]
    cmd = [dialogtype]
    if title:
        cmd += ["--title", title]
    if message:
        cmd += ["--message", message]
    if choices:
        cmd += ["--choices", ",".join(choices)]
    if backend:
        cmd += ["--backend", backend]
    if log.isEnabledFor(logging.DEBUG):
        cmd += ["--debug"]

    p = run_mod_as_subproc("psidialogs.cli.dialog", cmd)
    if p.return_code != 0:
        # log.debug(p)
        raise FailedBackendError(p)
    if dialogtype in ["message", "warning", "error"]:
        return None
    if dialogtype in ["ask_ok_cancel", "ask_yes_no"]:
        return p.stdout == "True"
    if p.stdout == "":
        return None
    return p.stdout
