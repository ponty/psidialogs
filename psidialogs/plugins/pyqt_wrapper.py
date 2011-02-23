from PyQt4 import QtGui
from yapsy.IPlugin import IPlugin


_app = None
class Backend(IPlugin):
    backend = 'PyQt'
    backend_version = 'not implemented'
    
    def __init__(self):
        #self.app = None
        pass
    
    def init_qt(self):
        global _app
        if not _app:
            _app = QtGui.QApplication(None)
            
    def message(self, args):
        self.init_qt()
        QtGui.QMessageBox.information(None, args.title, args.message)
    
    def warning(self, args):
        self.init_qt()
        QtGui.QMessageBox.warning(None, args.title, args.message)
    
    def error(self, args):
        self.init_qt()
        QtGui.QMessageBox.critical(None, args.title, args.message)
    
    def ask_ok_cancel(self, args):
        self.init_qt()
        reply = QtGui.QMessageBox.question(None, args.title, args.message, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        return (reply == QtGui.QMessageBox.Ok)
    
    def ask_yes_no(self, args):
        self.init_qt()
        reply = QtGui.QMessageBox.question(None, args.title, args.message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return (reply == QtGui.QMessageBox.Yes)
        
    def ask_folder(self, args):
        self.init_qt()
        result = QtGui.QFileDialog.getExistingDirectory(None, args.title,)
        if result:
            return str(result)
        
    def ask_file(self, args):
        self.init_qt()
        if args.save:
            result = QtGui.QFileDialog.getSaveFileName(None, args.title,)
        else:
            result = QtGui.QFileDialog.getOpenFileName(None, args.title,)
        if result:
            return str(result)

    def ask_string(self, args):
        self.init_qt()
        (result, ok) = QtGui.QInputDialog.getText(None, args.title, args.message,)
        if ok:
            return str(result)
        
    def choice(self, args):
        self.init_qt()
        (result, ok) = QtGui.QInputDialog.getItem(None, args.title, args.message, args.choices,)
        if ok:
            return str(result)
