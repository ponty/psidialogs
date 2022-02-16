from psidialogs.plugins.pyqt5base import PyQt5Base

# macos: brew install pyside@2
class PySide2Wrapper(PyQt5Base):
    name = "pyside2"
    # qt crashes after wx
    need_subprocess = True

    def __init__(self):
        from PySide2 import QtWidgets  # type: ignore

        self.QtWidgets = QtWidgets

    def backend_version(self):
        import PySide2

        return PySide2.__version__
