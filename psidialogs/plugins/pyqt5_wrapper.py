from psidialogs.iplugin import IPlugin


_app = None


class Backend(IPlugin):
    backend = "PyQt"
    name = "pyqt5"

    def __init__(self):
        from PyQt5 import QtWidgets
        self.QtWidgets = QtWidgets

    def backend_version(self):
        from PyQt5 import Qt
        return Qt.PYQT_VERSION_STR

    def init_qt(self):
        global _app
        if not _app:
            _app = self.QtWidgets.QApplication([])

    def message(self, args):
        self.init_qt()
        self.QtWidgets.QMessageBox.information(None, args["title"], args["message"])

    def warning(self, args):
        self.init_qt()
        self.QtWidgets.QMessageBox.warning(None, args["title"], args["message"])

    def error(self, args):
        self.init_qt()
        self.QtWidgets.QMessageBox.critical(None, args["title"], args["message"])

    def ask_ok_cancel(self, args):
        self.init_qt()
        reply = self.QtWidgets.QMessageBox.question(
            None,
            args["title"],
            args["message"],
            self.QtWidgets.QMessageBox.Ok,
            self.QtWidgets.QMessageBox.Cancel,
        )
        return reply == self.QtWidgets.QMessageBox.Ok

    def ask_yes_no(self, args):
        self.init_qt()
        reply = self.QtWidgets.QMessageBox.question(
            None,
            args["title"],
            args["message"],
            self.QtWidgets.QMessageBox.Yes,
            self.QtWidgets.QMessageBox.No,
        )
        return reply == self.QtWidgets.QMessageBox.Yes

    def ask_folder(self, args):
        self.init_qt()
        result = self.QtWidgets.QFileDialog.getExistingDirectory(None, args["title"],)
        if result:
            return "%s" % result

    def ask_file(self, args):
        self.init_qt()
        if args["save"]:
            result = self.QtWidgets.QFileDialog.getSaveFileName(None, args["title"],)
        else:
            result = self.QtWidgets.QFileDialog.getOpenFileName(None, args["title"],)
        if result:
            return "%s" % result[0]

    def ask_string(self, args):
        self.init_qt()
        (result, ok) = self.QtWidgets.QInputDialog.getText(
            None, args["title"], args["message"],
        )
        if ok:
            return "%s" % result

    def choice(self, args):
        self.init_qt()
        (result, ok) = self.QtWidgets.QInputDialog.getItem(
            None, args["title"], args["message"], args["choices"],
        )
        if ok:
            return "%s" % result
