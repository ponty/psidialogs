import logging
import os, psidialogs
from time import sleep
from PIL import Image, ImageChops

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from psidialogs.backendloader import BackendLoader

from pyvirtualdisplay.smartdisplay import SmartDisplay

# (cmd,grab,background)
commands = [
    ("python3 -m psidialogs.examples.demo --help", False, False),
]


def screenshot(cmd, fname):
    logging.info("%s %s", cmd, fname)
    # fpath = "docs/_img/%s" % fname
    # if os.path.exists(fpath):
    #     os.remove(fpath)
    with SmartDisplay() as disp:
        with EasyProcess(cmd):
            img = disp.waitgrab()
            img.save(fname)


def autocrop(im, bgcolor):
    if im.mode != "RGB":
        im = im.convert("RGB")
    bg = Image.new("RGB", im.size, bgcolor)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return None  # no contents


@entrypoint
def main():
    logging.info("commands: %s", commands)
    pls = []
    try:
        os.chdir("gen")
        for cmd, grab, bg in commands:
            with SmartDisplay() as disp:
                logging.info("======== cmd: %s", cmd)
                fname_base = cmd.replace(" ", "_")
                fname = fname_base + ".txt"
                # logging.info("cmd: %s", cmd)
                print("file name: %s" % fname)
                with open(fname, "w") as f:
                    f.write("$ " + cmd + "\n")
                    if bg:
                        p = EasyProcess(cmd).start()
                    else:
                        p = EasyProcess(cmd).call()
                        f.write(p.stdout)
                        f.write(p.stderr)
                    pls += [p]
                if grab:
                    png = fname_base + ".png"
                    sleep(1)
                    img = disp.waitgrab(timeout=9)
                    logging.info("saving %s", png)
                    img.save(png)
        for b in sorted(BackendLoader().all_names):
            for func in psidialogs.FUNCTION_NAMES:
                cmd = [
                    "python3",
                    "-m",
                    "psidialogs.examples.demo",
                    "-b",
                    b,
                    "-f",
                    func,
                    # "--debug",
                ]
                if BackendLoader().is_console(b):
                    # xterm -e python3 -m psidialogs.examples.demo -b zenity -f ask_yes_no
                    cmd = ["xterm", "-e", " ".join(cmd)]
                with SmartDisplay() as disp:
                    logging.info("======== cmd: %s", cmd)
                    with EasyProcess(cmd):
                        png = b + "_" + func + ".png"
                        sleep(0.1)
                        img = disp.waitgrab(timeout=9)
                        logging.info("saving %s", png)
                        if b == "console":
                            img = autocrop(img, (255, 255, 255))
                        if b == "pythondialog":
                            img = autocrop(img, (255, 255, 255))
                            img = autocrop(img, (0, 0, 238))
                        img.save(png)

    finally:
        os.chdir("..")
        for p in pls:
            p.stop()
    embedme = EasyProcess(["npx", "embedme", "../README.md"])
    embedme.call()
    print(embedme.stdout)
    assert embedme.return_code == 0
    assert not "but file does not exist" in embedme.stdout
