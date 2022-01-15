from psidialogs.plugins.pyqt5base import PyQt5Base


class PyQt5Wrapper(PyQt5Base):
    name = "pyqt5"

    def __init__(self):
        from PyQt5 import QtWidgets  # type: ignore

        self.QtWidgets = QtWidgets

    def backend_version(self):
        from PyQt5 import Qt

        return Qt.PYQT_VERSION_STR
