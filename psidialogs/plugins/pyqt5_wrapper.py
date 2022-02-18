from psidialogs.plugins.pyqt5base import PyQt5Base

# macos:  brew install pyqt@5
class PyQt5Wrapper(PyQt5Base):
    name = "pyqt5"
    # qt crashes after wx
    # need_subprocess = True

    def __init__(self):
        from PyQt5 import QtWidgets  # type: ignore

        self.QtWidgets = QtWidgets

    def backend_version(self):
        from PyQt5 import Qt

        return Qt.PYQT_VERSION_STR
