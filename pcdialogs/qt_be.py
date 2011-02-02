from PyQt4 import QtGui

app = QtGui.QApplication(None)
class Backend():
    def message(self, args):
        reply = QtGui.QMessageBox.information(None, args.title,   args.message)
    def warning(self, args):
        reply = QtGui.QMessageBox.warning(None, args.title,   args.message)
    def error(self, args):
        reply = QtGui.QMessageBox.critical(None, args.title,   args.message)
        
    def ask_ok_cancel(self, args):
        reply = QtGui.QMessageBox.question(None, args.title,   args.message, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        return (reply == QtGui.QMessageBox.Ok)
    
    def ask_yes_no(self, args):
        reply = QtGui.QMessageBox.question(None, args.title,   args.message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return (reply == QtGui.QMessageBox.Yes)
        
    def ask_folder(self, args):
        result= QtGui.QFileDialog.getExistingDirectory(None, args.title,)
        if result:
            return str(result)
        
    def ask_file(self, args):
        if args.save:
            result= QtGui.QFileDialog.getSaveFileName(None, args.title,)
        else:
            result= QtGui.QFileDialog.getOpenFileName(None, args.title,)
        if result:
            return str(result)

    def ask_files(self, args):
        result = QtGui.QFileDialog.getOpenFileNames(None, args.title,)
        if result:
            return [ str(x) for x in result ]
        
    def ask_string(self, args):
        (result, ok) =  QtGui.QInputDialog.getText(None, args.title,  args.message, )
        if ok:
            return str(result)
        
    def choice(self, args):
        (result, ok) =  QtGui.QInputDialog.getItem(None, args.title,  args.message, args.choices, )
        if ok:
            return str(result)
