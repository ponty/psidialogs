
from psidialogs.iplugin import IPlugin


_app = None


class Backend(IPlugin):
    backend = 'PyQt'
    name ='pyqt'

    def __init__(self):
        from PyQt4 import QtGui
        self.QtGui = QtGui

    def backend_version(self):
        return 'not implemented'

    def init_qt(self):
        global _app
        if not _app:
            _app = self.QtGui.QApplication(None)

    def message(self, args):
        self.init_qt()
        self.QtGui.QMessageBox.information(None, args.title, args.message)

    def warning(self, args):
        self.init_qt()
        self.QtGui.QMessageBox.warning(None, args.title, args.message)

    def error(self, args):
        self.init_qt()
        self.QtGui.QMessageBox.critical(None, args.title, args.message)

    def ask_ok_cancel(self, args):
        self.init_qt()
        reply = self.QtGui.QMessageBox.question(None,
                                                args.title,
                                                args.message,
                                                self.QtGui.QMessageBox.Ok,
                                                self.QtGui.QMessageBox.Cancel)
        return (reply == self.QtGui.QMessageBox.Ok)

    def ask_yes_no(self, args):
        self.init_qt()
        reply = self.QtGui.QMessageBox.question(None,
                                                args.title,
                                                args.message,
                                                self.QtGui.QMessageBox.Yes,
                                                self.QtGui.QMessageBox.No)
        return (reply == self.QtGui.QMessageBox.Yes)

    def ask_folder(self, args):
        self.init_qt()
        result = self.QtGui.QFileDialog.getExistingDirectory(None, args.title,)
        if result:
            return unicode(result)

    def ask_file(self, args):
        self.init_qt()
        if args.save:
            result = self.QtGui.QFileDialog.getSaveFileName(None, args.title,)
        else:
            result = self.QtGui.QFileDialog.getOpenFileName(None, args.title,)
        if result:
            return unicode(result)

    def ask_string(self, args):
        self.init_qt()
        (result, ok) = self.QtGui.QInputDialog.getText(None, args.title, args.message,)
        if ok:
            return unicode(result)

    def choice(self, args):
        self.init_qt()
        (result, ok) = self.QtGui.QInputDialog.getItem(None, args.title, args.message, args.choices,)
        if ok:
            return unicode(result)
