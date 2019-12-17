psidialogs (Python Simple Dialogs) is a common API
for different standard dialogs like message, ask_string,..

Links:
 * home: https://github.com/ponty/psidialogs
 * documentation: http://psidialogs.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/psidialogs

|Travis| |Latest Version| |Supported Python versions| |License| |Documentation|

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

Basic usage::

    >>> from psidialogs import message
    >>> message('Hello!')


Installation::

    pip install psidialogs

Install all back-ends on Ubuntu::

    sudo apt-get install python-gtk2
    sudo apt-get install python-tk
    sudo apt-get install python-qt4
    sudo apt-get install python-dialog
    sudo apt-get install zenity
    sudo apt-get install gxmessage
    sudo apt-get install python-easygui
    pip install --no-deps easydialogs-gtk

similar projects:
* `anygui <http://anygui.sourceforge.net/>`_: multiple back-ends
* `easygui <http://easygui.sourceforge.net/>`_: tk back-end
* `PyZenity <http://pypi.python.org/pypi/PyZenity>`_: Zenity back-end
* `vsgui <http://pypi.python.org/pypi/vsgui>`_: Zenity back-end
* `dlg <http://pypi.python.org/pypi/dlg>`_: dialog/Xdialog/gdialog  back-end
* `python-dialog <http://pypi.python.org/pypi/pythondialog>`_: dialog/Xdialog/gdialog  back-end
* `easydialogs-gtk <http://pypi.python.org/pypi/easydialogs-gtk>`_: EasyDialogs API, PyGTK back-end
* `EasyDialogs <http://docs.python.org/library/easydialogs.html>`_: EasyDialogs API, Mac back-end
* `EasyDialogs for Windows <http://pypi.python.org/pypi/EasyDialogs%20for%20Windows>`_: EasyDialogs API, Windows back-end



.. |Travis| image:: http://img.shields.io/travis/ponty/psidialogs.svg
   :target: https://travis-ci.org/ponty/psidialogs/
.. |Latest Version| image:: https://img.shields.io/pypi/v/psidialogs.svg
   :target: https://pypi.python.org/pypi/psidialogs/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/psidialogs.svg
   :target: https://pypi.python.org/pypi/psidialogs/
.. |License| image:: https://img.shields.io/pypi/l/psidialogs.svg
   :target: https://pypi.python.org/pypi/psidialogs/
.. |Documentation| image:: https://readthedocs.org/projects/psidialogs/badge/?version=latest
   :target: https://readthedocs.org/projects/psidialogs/?badge=latest
