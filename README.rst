psidialogs (Python Simple Dialogs) is a common API
for different standard dialogs like:

 - message
 - warning
 - ask_string
 - ...

Backends:
 - PyGTK
 - Zenity
 - easygui
 - gMessage
 - PyQt
 - TkInter
 - wxPython
 - ...

source: https://github.com/ponty/psidialogs

documentation: http://ponty.github.com/psidialogs

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

