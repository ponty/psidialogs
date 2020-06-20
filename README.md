psidialogs (Python Simple Dialogs) is a common API
for different standard dialogs like message, ask_string,..

Links:
 * home: https://github.com/ponty/psidialogs
 * PYPI: https://pypi.python.org/pypi/psidialogs

[![Build Status](https://travis-ci.org/ponty/psidialogs.svg?branch=master)](https://travis-ci.org/ponty/psidialogs)

back-ends:
 - PyGTK
 - Zenity
 - easygui
 - gMessage
 - PyQt
 - TkInter
 - wxPython
 - PythonDialog
 - console

Basic usage:
```pycon
>>> from psidialogs import message
>>> message('Hello!')
```


Installation:

```console
$ python3 -m pip install psidialogs
```

Install all back-ends on Ubuntu:

```console
$ sudo apt-get install python-gtk2
$ sudo apt-get install python-tk
$ sudo apt-get install python-qt4
$ sudo apt-get install python-dialog
$ sudo apt-get install zenity
$ sudo apt-get install gxmessage
$ sudo apt-get install python-easygui
```

similar projects:
* [anygui](http://anygui.sourceforge.net/): multiple back-ends
* [easygui](http://easygui.sourceforge.net/): tk back-end
* [PyZenity](http://pypi.python.org/pypi/PyZenity): Zenity back-end
* [vsgui](http://pypi.python.org/pypi/vsgui): Zenity back-end
* [dlg](http://pypi.python.org/pypi/dlg): dialog/Xdialog/gdialog  back-end
* [python-dialog](http://pypi.python.org/pypi/pythondialog): dialog/Xdialog/gdialog  back-end
