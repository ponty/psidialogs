from psidialogs.iplugin import IPlugin
from psidialogs.util import platform_is_osx
import logging

import ctypes

log = logging.getLogger(__name__)

##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel
##  6 : Cancel | Try Again | Continue

## To also change icon, add these values to previous number
# 16 Stop-sign icon
# 32 Question-mark icon
# 48 Exclamation-point icon
# 64 Information-sign icon consisting of an 'i' in a circle


## yes=6 no=7 ok=1 cancel=2


class Pywin32Wrapper(IPlugin):
    name = "pywin32"

    def __init__(self):
        import pywin.dialogs.list
        import win32gui
        import pywintypes
        from win32com.shell import shell
        import win32ui
        import win32con
        from pywin.mfc import dialog

        self.list = pywin.dialogs.list
        self.win32gui = win32gui
        self.pywintypes = pywintypes
        self.shell = shell
        self.win32ui = win32ui
        self.win32con = win32con
        self.dialog = dialog

    def backend_version(self):
        build_no = (
            open(os.path.join(site_packages, "pywin32.version.txt")).read().strip()
        )
        return build_no

    def ask_string(self, message, title):
        # https://github.com/mhammond/pywin32/blob/main/Pythonwin/pywin/dialogs/login.py
        from psidialogs.plugins.pywin32_ask_string import LoginDlg

        d = LoginDlg(title, message)
        d["inputid"] = ""
        if d.DoModal() == self.win32con.IDOK:
            ret = d["inputid"]
            if ret:
                return ret

    def message(self, message, title):
        style = 0 + 64
        ctypes.windll.user32.MessageBoxW(0, message, title, style)

    def error(self, message, title):
        style = 0 + 16
        ctypes.windll.user32.MessageBoxW(0, message, title, style)

    def warning(self, message, title):
        style = 0 + 48
        ctypes.windll.user32.MessageBoxW(0, message, title, style)

    def ask_ok_cancel(self, message, title):
        style = 1 + 64
        rc = ctypes.windll.user32.MessageBoxW(0, message, title, style)
        if rc == 1:
            return True
        return False

    def ask_yes_no(self, message, title):
        style = 4 + 64
        rc = ctypes.windll.user32.MessageBoxW(0, message, title, style)
        if rc == 6:
            return True
        return False

    def ask_file(self, message, title):
        # https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
        try:
            fname, _, _ = self.win32gui.GetOpenFileNameW(Title=title)
            return fname
        except self.pywintypes.error as e:
            log.error(e)
            return None

    def ask_folder(self, message, title):
        # https://github.com/mhammond/pywin32/blob/main/com/win32comext/shell/demos/browse_for_folder.py

        pidl, _, _ = self.shell.SHBrowseForFolder(
            0,  #  HWND
            None,  #  PIDL.
            title,
        )

        if pidl:
            try:
                my_path = self.shell.SHGetPathFromIDList(pidl).decode("utf-8")
                return my_path
            except Exception as e:
                log.error(e)

    def choice(self, choices, message, title):
        ## https://stackoverflow.com/questions/68469243/dialog-box-to-select-option-from-list-in-python-on-windows
        # TODO: add message
        result = self.list.SelectFromList(title, choices)
        if result is None:
            return None
        return choices[result]
