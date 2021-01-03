import sys

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

VISIBLE = 0
TIMEOUT = 5


def check_open(dialogtype):
    cmd = [
        sys.executable,
        "-c",
        "import psidialogs,logging;logging.basicConfig(level=logging.DEBUG);psidialogs.{dialogtype}".format(
            dialogtype=dialogtype
        ),
    ]
    # exception if nothing is displayed
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(cmd):
            disp.waitgrab(timeout=TIMEOUT)


def test_message():
    check_open("""message(message='hi')""")


def test_ask_string():
    check_open("""ask_string(message='hi')""")


def test_ask_file():
    check_open("""ask_file(message='hi')""")


def test_ask_folder():
    check_open("""ask_folder(message='hi')""")


def test_choice():
    check_open("""choice(message='hi',choices=['a','b'])""")


# def test_multi_choice():
#     check_open("""multi_choice(message='hi',choices=['a','b'])""")


# def test_text():
#     check_open("""text(text='hi')""")


def test_error():
    check_open("""error(message='hi')""")


def test_warning():
    check_open("""warning(message='hi')""")


def test_ask_ok_cancel():
    check_open("""ask_ok_cancel(message='hi')""")


def test_ask_yes_no():
    check_open("""ask_yes_no(message='hi')""")
