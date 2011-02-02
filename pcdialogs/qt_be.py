from PyQt4 import QtGui

app = QtGui.QApplication(None)
class Backend():
    def message(self, args):
        reply = QtGui.QMessageBox.information(None, args.title,   args.message)
    def warning(self, args):
        reply = QtGui.QMessageBox.warning(None, args.title,   args.message)
    def error(self, args):
        reply = QtGui.QMessageBox.critical(None, args.title,   args.message)
        
    def askOkCancel(self, args):
        reply = QtGui.QMessageBox.question(None, args.title,   args.message, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        return (reply == QtGui.QMessageBox.Ok)
    
    def askYesNo(self, args):
        reply = QtGui.QMessageBox.question(None, args.title,   args.message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return (reply == QtGui.QMessageBox.Yes)
        
    def askFolder(self, args):
        result= QtGui.QFileDialog.getExistingDirectory(None, args.title,)
        if result:
            return str(result)
        
    def askFileForSave(self, args):
        result= QtGui.QFileDialog.getSaveFileName(None, args.title,)
        if result:
            return str(result)
        

    def askFileForOpen(self, args):
        result= QtGui.QFileDialog.getOpenFileName(None, args.title,)
        if result:
            return str(result)
        
    def askFilesForOpen(self, args):
        result = QtGui.QFileDialog.getOpenFileNames(None, args.title,)
        if result:
            return [ str(x) for x in result ]
        
    def askString(self, args):
        (result, ok) =  QtGui.QInputDialog.getText(None, args.title,  args.message, )
        if ok:
            return str(result)
        
    def choice(self, args):
        (result, ok) =  QtGui.QInputDialog.getItem(None, args.title,  args.message, args.choices, )
        if ok:
            return str(result)
