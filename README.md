psidialogs (Python Simple Dialogs) is a wrapper
for different standard dialogs: 
 message, warning, error, ask_ok_cancel, ask_yes_no, ask_string, 
 ask_file, ask_folder, choice.


Links:
 * home: https://github.com/ponty/psidialogs
 * PYPI: https://pypi.python.org/pypi/psidialogs

[![Build Status](https://travis-ci.org/ponty/psidialogs.svg?branch=master)](https://travis-ci.org/ponty/psidialogs)

back-ends:
 - [Zenity](https://en.wikipedia.org/wiki/Zenity)
 - [easygui](http://easygui.sourceforge.net/)
 - gMessage
 - [PyQt5](https://pypi.org/project/PyQt5/)
 - [PySide2](https://pypi.org/project/PySide2/)
 - [TkInter](https://docs.python.org/3/library/tkinter.html)
 - [wxPython](https://www.wxpython.org/)
 - [PythonDialog](https://pypi.org/project/pythondialog/)
 - console

Usage:
```pycon
>>> from psidialogs import message
>>> message('Hello!')
```


Installation:

```console
$ python3 -m pip install psidialogs
```

Install all back-ends on Ubuntu 20.04:

```console
$ sudo apt-get install python3-tk
$ sudo apt-get install python3-pyqt5
$ sudo apt-get install python3-pyside2.qtwidgets
$ sudo apt-get install python3-dialog
$ sudo apt-get install python3-easygui
$ sudo apt-get install python3-wxgtk4.0
$ sudo apt-get install zenity
$ sudo apt-get install gxmessage
```

# Demo

All backends and all functions can be tested with the demo:

```console
$ python3 -m psidialogs.examples.demo
```

The demo can be started with one backend:
```console
$ python3 -m psidialogs.examples.demo --backend zenity
```

The demo can be started with one backend and one function:
```console
$ python3 -m psidialogs.examples.demo --backend zenity --function message
```

<!-- embedme doc/gen/python3_-m_psidialogs.examples.demo_--help.txt -->
Demo full help:

```console
$ python3 -m psidialogs.examples.demo --help
usage: demo.py [-h] [-b BACKEND] [-f FUNCTION] [-t TITLE] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -b BACKEND, --backend BACKEND
  -f FUNCTION, --function FUNCTION
  -t TITLE, --title TITLE
  --debug               set logging level to DEBUG
```

# Screenshots

Screenshots are created on Ubuntu 20.04 server with Xvfb.

Versions:
<!-- embedme doc/gen/python3_-m_psidialogs.check.versions.txt -->

```console
$ python3 -m psidialogs.check.versions
python               3.8.5
psidialogs           0.2.0
pyside2              5.14.0
tkinter              8.6
zenity               3.32.0
```

 ## message(), warning(), error() 

|      backend | message                               | warning                               | error                               |
| -----------: | ------------------------------------- | ------------------------------------- | ----------------------------------- |
|       zenity | ![](doc/gen/zenity_message.png)       | ![](doc/gen/zenity_warning.png)       | ![](doc/gen/zenity_error.png)       |
|     gmessage | ![](doc/gen/gmessage_message.png)     | ![](doc/gen/gmessage_warning.png)     | ![](doc/gen/gmessage_error.png)     |
|     wxpython | ![](doc/gen/wxpython_message.png)     | ![](doc/gen/wxpython_warning.png)     | ![](doc/gen/wxpython_error.png)     |
|      tkinter | ![](doc/gen/tkinter_message.png)      | ![](doc/gen/tkinter_warning.png)      | ![](doc/gen/tkinter_error.png)      |
|      easygui | ![](doc/gen/easygui_message.png)      | ![](doc/gen/easygui_warning.png)      | ![](doc/gen/easygui_error.png)      |
|        pyqt5 | ![](doc/gen/pyqt5_message.png)        | ![](doc/gen/pyqt5_warning.png)        | ![](doc/gen/pyqt5_error.png)        |
|      pyside2 | ![](doc/gen/pyside2_message.png)      | ![](doc/gen/pyside2_warning.png)      | ![](doc/gen/pyside2_error.png)      |
| pythondialog | ![](doc/gen/pythondialog_message.png) | ![](doc/gen/pythondialog_warning.png) | ![](doc/gen/pythondialog_error.png) |
|      console | ![](doc/gen/console_message.png)      | ![](doc/gen/console_warning.png)      | ![](doc/gen/console_error.png)      |

## ask_ok_cancel(), ask_yes_no(), ask_string()

|      backend | ask_ok_cancel                               | ask_yes_no                               | ask_string                               |
| -----------: | ------------------------------------------- | ---------------------------------------- | ---------------------------------------- |
|       zenity | ![](doc/gen/zenity_ask_ok_cancel.png)       | ![](doc/gen/zenity_ask_yes_no.png)       | ![](doc/gen/zenity_ask_string.png)       |
|     gmessage | ![](doc/gen/gmessage_ask_ok_cancel.png)     | ![](doc/gen/gmessage_ask_yes_no.png)     | ![](doc/gen/gmessage_ask_string.png)     |
|     wxpython | ![](doc/gen/wxpython_ask_ok_cancel.png)     | ![](doc/gen/wxpython_ask_yes_no.png)     | ![](doc/gen/wxpython_ask_string.png)     |
|      tkinter | ![](doc/gen/tkinter_ask_ok_cancel.png)      | ![](doc/gen/tkinter_ask_yes_no.png)      | ![](doc/gen/tkinter_ask_string.png)      |
|      easygui | ![](doc/gen/easygui_ask_ok_cancel.png)      | ![](doc/gen/easygui_ask_yes_no.png)      | ![](doc/gen/easygui_ask_string.png)      |
|        pyqt5 | ![](doc/gen/pyqt5_ask_ok_cancel.png)        | ![](doc/gen/pyqt5_ask_yes_no.png)        | ![](doc/gen/pyqt5_ask_string.png)        |
|      pyside2 | ![](doc/gen/pyside2_ask_ok_cancel.png)      | ![](doc/gen/pyside2_ask_yes_no.png)      | ![](doc/gen/pyside2_ask_string.png)      |
| pythondialog | ![](doc/gen/pythondialog_ask_ok_cancel.png) | ![](doc/gen/pythondialog_ask_yes_no.png) | ![](doc/gen/pythondialog_ask_string.png) |
|      console | ![](doc/gen/console_ask_ok_cancel.png)      | ![](doc/gen/console_ask_yes_no.png)      | ![](doc/gen/console_ask_string.png)      |

## ask_file(), ask_folder()

|      backend | ask_file                               | ask_folder                               |
| -----------: | -------------------------------------- | ---------------------------------------- |
|       zenity | ![](doc/gen/zenity_ask_file.png)       | ![](doc/gen/zenity_ask_folder.png)       |
|     gmessage | ![](doc/gen/gmessage_ask_file.png)     | ![](doc/gen/gmessage_ask_folder.png)     |
|     wxpython | ![](doc/gen/wxpython_ask_file.png)     | ![](doc/gen/wxpython_ask_folder.png)     |
|      tkinter | ![](doc/gen/tkinter_ask_file.png)      | ![](doc/gen/tkinter_ask_folder.png)      |
|      easygui | ![](doc/gen/easygui_ask_file.png)      | ![](doc/gen/easygui_ask_folder.png)      |
|        pyqt5 | ![](doc/gen/pyqt5_ask_file.png)        | ![](doc/gen/pyqt5_ask_folder.png)        |
|      pyside2 | ![](doc/gen/pyside2_ask_file.png)      | ![](doc/gen/pyside2_ask_folder.png)      |
| pythondialog | ![](doc/gen/pythondialog_ask_file.png) | ![](doc/gen/pythondialog_ask_folder.png) |
|      console | ![](doc/gen/console_ask_file.png)      | ![](doc/gen/console_ask_folder.png)      |

## choice()

|      backend | choice                               |
| -----------: | ------------------------------------ |
|       zenity | ![](doc/gen/zenity_choice.png)       |
|     gmessage | ![](doc/gen/gmessage_choice.png)     |
|     wxpython | ![](doc/gen/wxpython_choice.png)     |
|      tkinter | ![](doc/gen/tkinter_choice.png)      |
|      easygui | ![](doc/gen/easygui_choice.png)      |
|        pyqt5 | ![](doc/gen/pyqt5_choice.png)        |
|      pyside2 | ![](doc/gen/pyside2_choice.png)      |
| pythondialog | ![](doc/gen/pythondialog_choice.png) |
|      console | ![](doc/gen/console_choice.png)      |

