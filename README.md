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
 - EasyDialogs

Basic usage:
```pycon
>>> from psidialogs import message
>>> message('Hello!')
```


Installation:

```console
$ pip install psidialogs
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
$ python3 -m pip install --no-deps easydialogs-gtk
```

similar projects:
* [anygui](http://anygui.sourceforge.net/): multiple back-ends
* [easygui](http://easygui.sourceforge.net/): tk back-end
* [PyZenity](http://pypi.python.org/pypi/PyZenity): Zenity back-end
* [vsgui](http://pypi.python.org/pypi/vsgui): Zenity back-end
* [dlg](http://pypi.python.org/pypi/dlg): dialog/Xdialog/gdialog  back-end
* [python-dialog](http://pypi.python.org/pypi/pythondialog): dialog/Xdialog/gdialog  back-end
* [easydialogs-gtk](http://pypi.python.org/pypi/easydialogs-gtk): EasyDialogs API, PyGTK back-end
* [EasyDialogs](http://docs.python.org/library/easydialogs.html): EasyDialogs API, Mac back-end
* [EasyDialogs for Windows](http://pypi.python.org/pypi/EasyDialogs%20for%20Windows): EasyDialogs API, Windows back-end
