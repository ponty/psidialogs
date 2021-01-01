import logging
import os
from tempfile import TemporaryDirectory

from psidialogs.err import FailedBackendError
from psidialogs.util import run_mod_as_subproc

log = logging.getLogger(__name__)


def childprocess_backend_version(backend):
    p = run_mod_as_subproc("psidialogs.cli.print_backend_version", [backend])
    if p.return_code != 0:
        log.warning(p)
        raise FailedBackendError(p)

    return p.stdout


def childprocess_demo(backend, bbox):
    with TemporaryDirectory(prefix="psidialogs") as tmpdirname:
        filename = os.path.join(tmpdirname, "screenshot.png")
        cmd = ["--filename", filename]
        if backend:
            cmd += ["--backend", backend]
        if log.isEnabledFor(logging.DEBUG):
            cmd += ["--debug"]

        p = run_mod_as_subproc("psidialogs.examples.demo", cmd)
        if p.return_code != 0:
            # log.debug(p)
            raise FailedBackendError(p)

        return data
