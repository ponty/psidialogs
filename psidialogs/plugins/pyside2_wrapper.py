from psidialogs.plugins.pyqt5base import PyQt5Base


class PySide2Wrapper(PyQt5Base):
    name = "pyside2"

    def __init__(self):
        from PySide2 import QtWidgets

        self.QtWidgets = QtWidgets

    def backend_version(self):
        import PySide2

        return PySide2.__version__
