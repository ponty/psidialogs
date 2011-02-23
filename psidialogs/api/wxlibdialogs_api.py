import psidialogs
import wx

def textEntryDialog(parent=None, message='', title='', defaultText='', style=20):
    return psidialogs.ask_string(message=message, title=title, default=defaultText)

def dirDialog(parent=None, message='Choose a directory', path='', style=0, pos=wx.Point(-1, -1), size=wx.Size(-1, -1)):
    return psidialogs.ask_folder(message=message, default=path)

def colorDialog(parent=None, colorData=None, color=None):
    raise NotImplementedError()

def scrolledMessageDialog(parent=None, message='', title='', pos=wx.Point(-1, -1), size=(500, 300)):
    return psidialogs.text(text=message, title=title)

def colourDialog(parent=None, colourData=None, colour=None):
    raise NotImplementedError()

def alertDialog(parent=None, message='', title='Alert', pos=wx.Point(-1, -1)):
    return psidialogs.error(message=message, title=title)

def messageDialog(parent=None, message='', title='Message box', aStyle=21, pos=wx.Point(-1, -1)):
    return psidialogs.message(message=message, title=title)

def multipleChoiceDialog(parent=None, message='', title='', lst=[], pos=wx.Point(-1, -1), size=wx.Size(-1, -1)):
    return psidialogs.multi_choice(message=message, title=title, choices=lst)

def singleChoiceDialog(parent=None, message='', title='', lst=[], style=21):
    return psidialogs.choice(message=message, title=title, choices=lst)

def openFileDialog(parent=None, title='Open', directory='', filename='', wildcard='All Files (*.*)|*.*', style=33):
    return psidialogs.ask_file(title=title, default=filename, save=False)

def saveFileDialog(parent=None, title='Save', directory='', filename='', wildcard='All Files (*.*)|*.*', style=14):
    return psidialogs.ask_file(title=title, default=filename, save=True)

