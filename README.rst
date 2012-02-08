psidialogs (Python Simple Dialogs) is a common API
for different standard dialogs like message, ask_string,..

Links:
 * home: https://github.com/ponty/psidialogs
 * documentation: http://ponty.github.com/psidialogs


Backends:
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
 

Some dialogs are too simple, because a common basic
implementation is used where implementation is missing.


Basic usage
------------

    >>> from psidialogs import message
    >>> message('Hello!')


Installation
============

General
--------

 * install pip_
 * install the program::

    # as root
    pip install psidialogs

Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo pip install psidialogs

Uninstall
----------
::


    # as root
    pip uninstall psidialogs

similar projects
-------------------

* `anygui <http://anygui.sourceforge.net/>`_: multiple backends
* `easygui <http://easygui.sourceforge.net/>`_: tk backend
* `PyZenity <http://pypi.python.org/pypi/PyZenity>`_: Zenity backend
* `vsgui <http://pypi.python.org/pypi/vsgui>`_: Zenity backend
* `dlg <http://pypi.python.org/pypi/dlg>`_: dialog/Xdialog/gdialog  backend
* `python-dialog <http://pypi.python.org/pypi/pythondialog>`_: dialog/Xdialog/gdialog  backend
* `easydialogs-gtk <http://pypi.python.org/pypi/easydialogs-gtk>`_: EasyDialogs API, PyGTK backend
* `EasyDialogs <http://docs.python.org/library/easydialogs.html>`_: EasyDialogs API, Mac backend
* `EasyDialogs for Windows <http://pypi.python.org/pypi/EasyDialogs%20for%20Windows>`_: EasyDialogs API, Windows backend


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/

