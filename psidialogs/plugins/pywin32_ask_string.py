import win32ui

import win32con
from pywin.mfc import dialog


def MakeLoginDlgTemplate(title, msg):
    style = (
        win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE

    # Window frame and title
    dlg = [
        [title, (0, 0, 284, 40), style, None, (8, "MS Sans Serif")],
    ]

    # ID label and text box
    dlg.append([130, msg, -1, (7, 9, 203, 9), cs | win32con.SS_LEFT])
    s = cs | win32con.WS_TABSTOP | win32con.WS_BORDER
    dlg.append(["EDIT", None, win32ui.IDC_EDIT1, (7, 20, 203, 12), s])

    # OK/Cancel Buttons
    s = cs | win32con.WS_TABSTOP
    dlg.append(
        [128, "OK", win32con.IDOK, (224, 5, 50, 14), s | win32con.BS_DEFPUSHBUTTON]
    )
    s = win32con.BS_PUSHBUTTON | s
    dlg.append([128, "Cancel", win32con.IDCANCEL, (224, 20, 50, 14), s])
    return dlg


class LoginDlg(dialog.Dialog):
    Cancel = 0

    def __init__(self, title, msg):
        dialog.Dialog.__init__(self, MakeLoginDlgTemplate(title, msg))
        self.AddDDX(win32ui.IDC_EDIT1, "inputid")
