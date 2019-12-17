psidialogs (Python Simple Dialogs) is a common API
for different standard dialogs like message, ask_string,..

Links:
 * home: https://github.com/ponty/psidialogs
 * documentation: http://psidialogs.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/psidialogs

|Travis| |Coveralls| |Latest Version| |Supported Python versions| |License| |Code Health| |Documentation|

Features:
 - unicode support
 - cross-platform, development on linux
  
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
 
Known problems:
 - Python 3 is not supported
 - tested only on Linux and Windows

Some dialogs are too simple, because a common basic
implementation is used where implementation is missing.


Basic usage
-----------

    >>> from psidialogs import message
    >>> message('Hello!')


Installation
============

General
-------

 * install pip_
 * install the program::

    # as root
    pip install psidialogs

Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo pip install psidialogs
    # optional back-ends
    sudo apt-get install python-gtk2
    sudo apt-get install python-tk
    sudo apt-get install python-qt4
    sudo apt-get install python-dialog
    sudo apt-get install zenity
    sudo apt-get install gxmessage
    sudo apt-get install python-easygui
    sudo pip install --no-deps easydialogs-gtk


Uninstall
---------
::


    # as root
    pip uninstall psidialogs

similar projects
----------------

* `anygui <http://anygui.sourceforge.net/>`_: multiple back-ends
* `easygui <http://easygui.sourceforge.net/>`_: tk back-end
* `PyZenity <http://pypi.python.org/pypi/PyZenity>`_: Zenity back-end
* `vsgui <http://pypi.python.org/pypi/vsgui>`_: Zenity back-end
* `dlg <http://pypi.python.org/pypi/dlg>`_: dialog/Xdialog/gdialog  back-end
* `python-dialog <http://pypi.python.org/pypi/pythondialog>`_: dialog/Xdialog/gdialog  back-end
* `easydialogs-gtk <http://pypi.python.org/pypi/easydialogs-gtk>`_: EasyDialogs API, PyGTK back-end
* `EasyDialogs <http://docs.python.org/library/easydialogs.html>`_: EasyDialogs API, Mac back-end
* `EasyDialogs for Windows <http://pypi.python.org/pypi/EasyDialogs%20for%20Windows>`_: EasyDialogs API, Windows back-end


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/

.. |Travis| image:: http://img.shields.io/travis/ponty/psidialogs.svg
   :target: https://travis-ci.org/ponty/psidialogs/
.. |Coveralls| image:: http://img.shields.io/coveralls/ponty/psidialogs/master.svg
   :target: https://coveralls.io/r/ponty/psidialogs/
.. |Latest Version| image:: https://img.shields.io/pypi/v/psidialogs.svg
   :target: https://pypi.python.org/pypi/psidialogs/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/psidialogs.svg
   :target: https://pypi.python.org/pypi/psidialogs/
.. |License| image:: https://img.shields.io/pypi/l/psidialogs.svg
   :target: https://pypi.python.org/pypi/psidialogs/
.. |Code Health| image:: https://landscape.io/github/ponty/psidialogs/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ponty/psidialogs/master
.. |Documentation| image:: https://readthedocs.org/projects/psidialogs/badge/?version=latest
   :target: https://readthedocs.org/projects/psidialogs/?badge=latest
