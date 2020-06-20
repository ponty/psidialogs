import os
import sys

from easyprocess import EasyProcess


def py2():
    return sys.version_info[0] == 2


def py3():
    return sys.version_info[0] == 3


def py_minor():
    return sys.version_info[1]


def platform_is_osx():
    return sys.platform == "darwin"


def platform_is_win():
    return sys.platform == "win32"


def platform_is_linux():
    return sys.platform.startswith("linux")


def run_mod_as_subproc(name, params=[]):
    python = sys.executable
    cmd = [python, "-m", name] + params
    p = EasyProcess(cmd).call()
    return p

