psidialogs (Python Simple Dialogs) is a wrapper
for different standard dialogs: 
 message, warning, error, ask_ok_cancel, ask_yes_no, ask_string, 
 ask_file, ask_folder, choice.


Links:
 * home: https://github.com/ponty/psidialogs
 * PYPI: https://pypi.python.org/pypi/psidialogs

![workflow](https://github.com/ponty/psidialogs/actions/workflows/main.yml/badge.svg)

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

# Installation

```console
$ python3 -m pip install psidialogs
```

Install all back-ends on Ubuntu 22.04:

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

# Usage

```py
# psidialogs/examples/message.py

import psidialogs

psidialogs.message("Hello!")

```
![](doc/gen/python3_-m_psidialogs.examples.message.png)  

```py
# psidialogs/examples/warning.py

import psidialogs

psidialogs.warning("Warning text.")

```
![](doc/gen/python3_-m_psidialogs.examples.warning.png)  

```py
# psidialogs/examples/error.py

import psidialogs

psidialogs.error("Error text.")

```
![](doc/gen/python3_-m_psidialogs.examples.error.png)  

```py
# psidialogs/examples/ask_ok_cancel.py

import psidialogs

ok = psidialogs.ask_ok_cancel("Do you want to continue?")
if ok:
    print("continue")

```
![](doc/gen/python3_-m_psidialogs.examples.ask_ok_cancel.png)  

```py
# psidialogs/examples/ask_yes_no.py

import psidialogs

yes = psidialogs.ask_yes_no("Yes or no?")
if yes:
    print("yes!")

```
![](doc/gen/python3_-m_psidialogs.examples.ask_yes_no.png)  

```py
# psidialogs/examples/ask_string.py

import psidialogs

name = psidialogs.ask_string("What is your name?")
if name is not None:
    print(name)

```
![](doc/gen/python3_-m_psidialogs.examples.ask_string.png)  

```py
# psidialogs/examples/ask_file.py

import psidialogs

f = psidialogs.ask_file("Select a file!")
if f is not None:
    print(f)

```
![](doc/gen/python3_-m_psidialogs.examples.ask_file.png)  

```py
# psidialogs/examples/ask_folder.py

import psidialogs

f = psidialogs.ask_folder("Select a folder!")
if f is not None:
    print(f)

```
![](doc/gen/python3_-m_psidialogs.examples.ask_folder.png)  

```py
# psidialogs/examples/choice.py

import psidialogs

s = psidialogs.choice(["1", "2", "3"], "Choose a number!")
if s is not None:
    print(s)

```
![](doc/gen/python3_-m_psidialogs.examples.choice.png)  


The implemented backends can be listed, the order is the preference, which can be changed:
```py
# psidialogs/examples/backends.py

import psidialogs

print(psidialogs.backends())
psidialogs.set_backend_preference(["tkinter", "zenity"])
print(psidialogs.backends())

```
<!-- embedme doc/gen/python3_-m_psidialogs.examples.backends.txt -->
```console
$ python3 -m psidialogs.examples.backends
['pyside2', 'tkinter', 'zenity']
['tkinter', 'zenity', 'pyside2']
```


Changing the backend preference:
```py
# psidialogs/examples/set_backend_preference.py

import psidialogs

psidialogs.set_backend_preference(["tkinter", "zenity"])
psidialogs.message("Hello!")

```
![](doc/gen/python3_-m_psidialogs.examples.set_backend_preference.png)  


# Demo

<!-- embedme doc/gen/python3_-m_psidialogs.examples.demo.txt -->
All backends and all dialog types can be tested with the demo:
```console
$ python3 -m psidialogs.examples.demo
```
![](doc/gen/python3_-m_psidialogs.examples.demo.png)  

<!-- embedme doc/gen/python3_-m_psidialogs.examples.demo_--backend_zenity.txt -->
The demo can be started with one backend:
```console
$ python3 -m psidialogs.examples.demo --backend zenity
```
![](doc/gen/python3_-m_psidialogs.examples.demo_--backend_zenity.png)  

<!-- embedme doc/gen/python3_-m_psidialogs.examples.demo_--backend_zenity_--dialogtype_message.txt -->
The demo can be started with one backend and one dialog type:
```console
$ python3 -m psidialogs.examples.demo --backend zenity --dialogtype message
```
![](doc/gen/python3_-m_psidialogs.examples.demo_--backend_zenity_--dialogtype_message.png)  

<!-- embedme doc/gen/python3_-m_psidialogs.examples.demo_--help.txt -->
Demo full help:

```console
$ python3 -m psidialogs.examples.demo --help
usage: demo.py [-h] [-b BACKEND] [-d DIALOGTYPE] [-t TITLE] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -b BACKEND, --backend BACKEND
  -d DIALOGTYPE, --dialogtype DIALOGTYPE
  -t TITLE, --title TITLE
  --debug               set logging level to DEBUG
```

# Screenshots

Screenshots are created on Ubuntu 22.04 server with Xvfb.

Versions:
<!-- embedme doc/gen/python3_-m_psidialogs.check.versions.txt -->

```console
$ python3 -m psidialogs.check.versions
python               3.8.10
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

Hierarchy
=========

![Alt text](https://g.gravizo.com/source/svg?https%3A%2F%2Fraw.githubusercontent.com/ponty/psidialogs/master/doc/hierarchy.dot)
