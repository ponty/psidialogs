import platform
from entrypoint2 import entrypoint

import psidialogs
from psidialogs import backend_version


def print_name_version(name, version):
    s = "{:<20} {}".format(name, version)
    print(s)


@entrypoint
def print_versions():
    print_name_version("python", platform.python_version())
    print_name_version("psidialogs", psidialogs.__version__)

    for name in psidialogs.backends():
        v = backend_version(name)
        if not v:
            v = ""
        print_name_version(name, v)
