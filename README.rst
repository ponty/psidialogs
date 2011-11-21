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

 * install setuptools_ or pip_
 * install the program:

if you have setuptools_ installed::

    # as root
    easy_install psidialogs

if you have pip_ installed::

    # as root
    pip install psidialogs

Ubuntu
----------
::

    sudo apt-get install python-setuptools
    sudo easy_install psidialogs

Uninstall
----------
::


    # as root
    pip uninstall psidialogs


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/

