import glob
import logging
import os
from pathlib import Path
from threading import Thread
from time import sleep

from discogui.imgutil import grab_no_blink
from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from PIL import Image, ImageChops
from pyvirtualdisplay.smartdisplay import SmartDisplay

import psidialogs

# (cmd,grab,background)
commands = [
    ("python3 -m psidialogs.examples.demo --help", False, False),
    ("python3 -m psidialogs.check.versions", False, False),
    ("python3 -m psidialogs.examples.demo", True, True),
    ("python3 -m psidialogs.examples.demo --backend zenity", True, True),
    (
        "python3 -m psidialogs.examples.demo --backend zenity --function message",
        True,
        True,
    ),
]


def autocrop(im, bgcolor):
    if im.mode != "RGB":
        im = im.convert("RGB")
    bg = Image.new("RGB", im.size, bgcolor)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return None  # no contents


def empty_dir(dir):
    files = glob.glob(os.path.join(dir, "*"))
    for f in files:
        os.remove(f)


@entrypoint
def main():
    gendir = Path(__file__).absolute().parent / "gen"
    logging.info("gendir: %s", gendir)
    os.makedirs(gendir, exist_ok=True)
    empty_dir(gendir)
    logging.info("commands: %s", commands)
    try:
        cwd = os.getcwd()
        os.chdir("/bin")
        for cmd, grab, bg in commands:
            with SmartDisplay() as disp:
                logging.info("======== cmd: %s", cmd)
                fname_base = cmd.replace(" ", "_")
                fname = fname_base + ".txt"
                fname = gendir / fname
                # logging.info("cmd: %s", cmd)
                print("file name: %s" % fname)
                cons = "$ " + cmd
                try:
                    if bg:
                        p = EasyProcess(cmd).start()
                    else:
                        p = EasyProcess(cmd).call()
                        if p.stdout:
                            cons += "\n" + p.stdout
                        if p.stderr:
                            cons += "\n" + p.stderr
                    fname.write_text(cons)
                    if grab:
                        png = fname_base + ".png"
                        png = gendir / png
                        png = str(png)
                        sleep(1)
                        img = disp.waitgrab(timeout=9)
                        logging.info("saving %s", png)
                        img.save(png)
                finally:
                    p.stop()

        for backend in sorted(psidialogs.backends()):
            for func in psidialogs.FUNCTION_NAMES:
                # if BackendLoader().is_console(b):
                #     # xterm -e python3 -m psidialogs.examples.demo -b zenity -f ask_yes_no
                #     cmd = ["xterm", "-e", " ".join(cmd)]
                with SmartDisplay() as disp:
                    logging.info("======== func: %s backend: %s", func, backend)
                    t = Thread(
                        target=lambda: psidialogs.dialog(
                            func,
                            backend=backend,
                            message=u"This is the message. (%s,%s) \u20ac"
                            % (backend, func),
                            choices=["one", "two", "three"],
                        )
                    )
                    t.start()

                    png = backend + "_" + func + ".png"
                    png = os.path.join(gendir, png)
                    disp.waitgrab(timeout=9)
                    img = grab_no_blink()
                    logging.info("saving %s", png)
                    if backend == "console":
                        img = autocrop(img, (255, 255, 255))
                    if backend == "pythondialog":
                        img = autocrop(img, (255, 255, 255))
                        img = autocrop(img, (0, 0, 238))
                    img.save(png)
                t.join()
    finally:
        os.chdir(cwd)
        # for p in pls:
        #     p.stop()

    embedme = EasyProcess(["npx", "embedme", "../README.md"])
    embedme.call()
    print(embedme.stdout)
    assert embedme.return_code == 0
    assert not "but file does not exist" in embedme.stdout
