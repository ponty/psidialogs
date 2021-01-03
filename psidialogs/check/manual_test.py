import logging
import os
import tempfile
from pathlib import Path

from entrypoint2 import entrypoint

import psidialogs

log = logging.getLogger(__name__)

TITLE = "manual test"


def print_result(ok, ret, dtype, backend):
    print(
        "test result: {}     returned: {:<10} dtype: {:<15}  backend: {}".format(
            int(ok), repr(ret), dtype, backend
        )
    )


def button1():
    for dtype in ["message", "warning", "error"]:
        for backend in psidialogs.backends():
            ret = psidialogs.dialog(
                dtype, title=TITLE, backend=backend, message="Press the OK button!"
            )
            ok = ret == None
            print_result(ok, ret, dtype, backend)


def button2(i):
    button_labels = dict(ask_ok_cancel=("Cancel", "OK"), ask_yes_no=("No", "Yes"))

    for dtype in ["ask_ok_cancel", "ask_yes_no"]:
        for backend in psidialogs.backends():
            bname = button_labels[dtype][i]
            ret = psidialogs.dialog(
                dtype, title=TITLE, backend=backend, message=f"Press the {bname} button!"
            )
            ok = ret == [False, True][i]
            print_result(ok, ret, dtype, backend)


def buttonAsk(i, text=""):
    button_labels = dict(ask_string=("Cancel", "OK"))

    for dtype in ["ask_string"]:
        for backend in psidialogs.backends():
            bname = button_labels[dtype][i]
            t = ""
            if text:
                t = f"Type {text}! "
            ret = psidialogs.dialog(
                dtype,
                title=TITLE,
                backend=backend,
                message=t + f"Press the {bname} button!",
            )
            ok = ret == [None, text][i]
            print_result(ok, ret, dtype, backend)


def buttonChoice(i, text=""):
    button_labels = dict(choice=("Cancel", "OK"))

    for dtype in ["choice"]:
        for backend in psidialogs.backends():
            bname = button_labels[dtype][i]
            t = ""
            if text:
                t = f"Choose {text}! "
            ret = psidialogs.dialog(
                dtype,
                title=TITLE,
                backend=backend,
                message=t + f"Press the {bname} button!",
                choices=["1", "2", "3"],
            )
            ok = ret == [None, text][i]
            print_result(ok, ret, dtype, backend)


def buttonFile(i):
    with tempfile.TemporaryDirectory() as tmpdir:
        workdir = Path(tmpdir) / "test"
        workdir.mkdir()
        os.chdir(workdir)
        workfile = workdir / "hello.txt"
        workfile.write_text("hello")
        text = str(workfile)
        button_labels = dict(ask_file=("Cancel", "OK"))

        for dtype in ["ask_file"]:
            for backend in psidialogs.backends():
                bname = button_labels[dtype][i]
                t = ""
                if i:
                    t = f"Choose {text}! "
                ret = psidialogs.dialog(
                    dtype,
                    # title=TITLE,
                    backend=backend,
                    title=t + f"Press the {bname} button!",
                    choices=["1", "2", "3"],
                )
                ok = ret == [None, text][i]
                print_result(ok, ret, dtype, backend)


def buttonDir(i):
    with tempfile.TemporaryDirectory() as tmpdir:
        workdir = Path(tmpdir) / "test"
        workdir.mkdir()
        os.chdir(tmpdir)
        workfile = workdir / "hello.txt"
        workfile.write_text("hello")
        text = str(workdir)
        button_labels = dict(ask_folder=("Cancel", "OK"))

        for dtype in ["ask_folder"]:
            for backend in psidialogs.backends():
                bname = button_labels[dtype][i]
                t = ""
                if i:
                    t = f"Choose {text}! "
                ret = psidialogs.dialog(
                    dtype,
                    # title=TITLE,
                    backend=backend,
                    title=t + f"Press the {bname} button!",
                    choices=["1", "2", "3"],
                )
                ok = ret == [None, text][i]
                print_result(ok, ret, dtype, backend)


@entrypoint
def dialog_cli(step=0):
    # with Display(visible=1):
    if not step or step == 1:
        button1()
    if not step or step == 2:
        button2(0)
    if not step or step == 3:
        button2(1)
    if not step or step == 4:
        buttonAsk(0)
    if not step or step == 5:
        buttonAsk(1, "123")

    if not step or step == 6:
        buttonChoice(0)
    if not step or step == 7:
        buttonChoice(1, "2")

    if not step or step == 8:
        buttonFile(0)
    if not step or step == 9:
        buttonFile(1)

    if not step or step == 10:
        buttonDir(0)
    if not step or step == 11:
        buttonDir(1)
