from psidialogs.iplugin import IPlugin

_app = None


class PyQt5Base(IPlugin):
    QtWidgets = None

    def init_qt(self):
        global _app
        if not _app:
            _app = self.QtWidgets.QApplication([])

    def message(self, message, title):
        self.init_qt()
        self.QtWidgets.QMessageBox.information(None, title, message)

    def warning(self, message, title):
        self.init_qt()
        self.QtWidgets.QMessageBox.warning(None, title, message)

    def error(self, message, title):
        self.init_qt()
        self.QtWidgets.QMessageBox.critical(None, title, message)

    def ask_ok_cancel(self, message, title):
        self.init_qt()
        reply = self.QtWidgets.QMessageBox.question(
            None,
            title,
            message,
            self.QtWidgets.QMessageBox.Ok,
            self.QtWidgets.QMessageBox.Cancel,
        )
        return reply == self.QtWidgets.QMessageBox.Ok

    def ask_yes_no(self, message, title):
        self.init_qt()
        reply = self.QtWidgets.QMessageBox.question(
            None,
            title,
            message,
            self.QtWidgets.QMessageBox.Yes,
            self.QtWidgets.QMessageBox.No,
        )
        return reply == self.QtWidgets.QMessageBox.Yes

    def ask_folder(self, message, title):
        self.init_qt()
        result = self.QtWidgets.QFileDialog.getExistingDirectory(None, title,)
        if result:
            return "%s" % result

    def ask_file(self, message, title):
        self.init_qt()
        # if args["save"]:
        #     result = self.QtWidgets.QFileDialog.getSaveFileName(None, args["title"],)
        # else:
        result = self.QtWidgets.QFileDialog.getOpenFileName(None, title,)
        if result:
            return "%s" % result[0]

    def ask_string(self, message, title):
        self.init_qt()
        (result, ok) = self.QtWidgets.QInputDialog.getText(None, title, message,)
        if ok:
            return "%s" % result

    def choice(self, choices, message, title):
        self.init_qt()
        (result, ok) = self.QtWidgets.QInputDialog.getItem(
            None, title, message, choices, 0, False
        )
        if ok:
            return "%s" % result
