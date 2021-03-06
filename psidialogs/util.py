import sys

from easyprocess import EasyProcess


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


def check_import(module):
    found = False
    # try:
    #     __import__(module)

    #     ok = True
    # except ImportError:
    #     pass

    import importlib

    try:
        spam_spec = importlib.util.find_spec(module)
    except ModuleNotFoundError:
        return False
    found = spam_spec is not None
    return found


def prog_check(cmd):
    try:
        p = EasyProcess(cmd).call()
        if p.return_code == 0:
            return True
        return not p.oserror
    except Exception:
        return False


def extract_version(txt):
    """This function tries to extract the version from the help text of any
    program."""
    words = txt.replace(",", " ").split()
    version = None
    for x in reversed(words):
        if len(x) > 2:
            if x[0].lower() == "v":
                x = x[1:]
            if "." in x and x[0].isdigit():
                version = x
                break
    return version
