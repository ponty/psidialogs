app = None


def wx1():
    import wx.lib.dialogs

    global app
    app = wx.App()

    wx.lib.dialogs.messageDialog(
        message="message",
        title="title",
        aStyle=wx.OK | wx.CENTRE | wx.ICON_ERROR,
    )
    # app.Destroy()

    # app = None


def tk1():
    from tkinter import Label, Tk

    root = Tk()
    label = Label(root, text="hello")
    label.pack()

    root.mainloop()


def qt1():
    from PyQt5 import QtWidgets

    QtWidgets.QApplication([])

    # (result, ok) = QtWidgets.QInputDialog.getItem(
    #     None, " title", "message", ["choices"], 0, False
    # )

    QtWidgets.QMessageBox.information(None, "title", "message")


# import wx.lib.dialogs

# app = wx.App()
# wx.lib.dialogs.messageDialog(
#     message="message",
#     title="title",
#     aStyle=wx.OK | wx.CENTRE,
# )
# app.Destroy()
# time.sleep(1)

# from PyQt5 import QtWidgets
# q_app = QtWidgets.QApplication([])

# (result, ok) = QtWidgets.QInputDialog.getItem(
#     None, " title", "message", ["choices"], 0, False
# )

# QtWidgets.QMessageBox.information(None, "title", "message")

wx1()
qt1()
# tk1()
