Screenshots
==================================


..  [[[cog
..  import psidialogs
..  from psidialogs.backendloader import BackendLoader
..  backends=sorted(BackendLoader().all_names)
..  functions=psidialogs.FUNCTION_NAMES
..  for f in functions:
..    if 'file' in f or 'folder' in f:
..         continue
..    cog.outl('')
..    cog.outl('.. _%s:' % f)
..    cog.outl('')
..    cog.outl('------------------------')
..    cog.outl(f+'()')
..    cog.outl('------------------------')
..    cog.outl('')
..    cog.outl(':func:`API<psidialogs.%s>`' % f)
..    cog.outl('')
..    for b in backends:
..      cog.outl('')
..      cog.outl(b)
..      cog.outl('------------------------')
..      cog.outl('')
..      cmd = 'python -m psidialogs.examples.demo -b %s -f %s'  % (b,f)
..      if BackendLoader().is_console(b):
..         cmd='xterm -e "%s"' % cmd
..      cog.outl('.. program-screenshot:: ' + cmd )
..      #cog.outl('      :scale: 70 %')
..      cog.outl('      :prompt:')
..      #cog.outl('      :stdout:')
..      #cog.outl('      :stderr:')
..      cog.outl('      :wait: 1')
..      cog.outl('')
..  ]]]

.. _ask_ok_cancel:

------------------------
ask_ok_cancel()
------------------------

:func:`API<psidialogs.ask_ok_cancel>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f ask_ok_cancel"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f ask_ok_cancel
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f ask_ok_cancel
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f ask_ok_cancel
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f ask_ok_cancel
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f ask_ok_cancel"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f ask_ok_cancel
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f ask_ok_cancel
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f ask_ok_cancel
      :prompt:
      :wait: 1


.. _ask_string:

------------------------
ask_string()
------------------------

:func:`API<psidialogs.ask_string>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f ask_string"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f ask_string
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f ask_string
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f ask_string
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f ask_string
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f ask_string"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f ask_string
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f ask_string
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f ask_string
      :prompt:
      :wait: 1


.. _ask_yes_no:

------------------------
ask_yes_no()
------------------------

:func:`API<psidialogs.ask_yes_no>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f ask_yes_no"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f ask_yes_no
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f ask_yes_no
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f ask_yes_no
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f ask_yes_no
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f ask_yes_no"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f ask_yes_no
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f ask_yes_no
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f ask_yes_no
      :prompt:
      :wait: 1


.. _choice:

------------------------
choice()
------------------------

:func:`API<psidialogs.choice>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f choice"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f choice
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f choice
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f choice
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f choice
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f choice"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f choice
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f choice
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f choice
      :prompt:
      :wait: 1


.. _error:

------------------------
error()
------------------------

:func:`API<psidialogs.error>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f error"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f error
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f error
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f error
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f error
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f error"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f error
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f error
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f error
      :prompt:
      :wait: 1


.. _message:

------------------------
message()
------------------------

:func:`API<psidialogs.message>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f message"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f message
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f message
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f message
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f message
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f message"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f message
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f message
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f message
      :prompt:
      :wait: 1


.. _multi_choice:

------------------------
multi_choice()
------------------------

:func:`API<psidialogs.multi_choice>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f multi_choice"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f multi_choice
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f multi_choice
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f multi_choice
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f multi_choice
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f multi_choice"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f multi_choice
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f multi_choice
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f multi_choice
      :prompt:
      :wait: 1


.. _text:

------------------------
text()
------------------------

:func:`API<psidialogs.text>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f text"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f text
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f text
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f text
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f text
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f text"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f text
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f text
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f text
      :prompt:
      :wait: 1


.. _warning:

------------------------
warning()
------------------------

:func:`API<psidialogs.warning>`


console
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b console -f warning"
      :prompt:
      :wait: 1


easygui
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b easygui -f warning
      :prompt:
      :wait: 1


gmessage
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b gmessage -f warning
      :prompt:
      :wait: 1


pygtk
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pygtk -f warning
      :prompt:
      :wait: 1


pyqt
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b pyqt -f warning
      :prompt:
      :wait: 1


pythondialog
------------------------

.. program-screenshot:: xterm -e "python -m psidialogs.examples.demo -b pythondialog -f warning"
      :prompt:
      :wait: 1


tkinter
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b tkinter -f warning
      :prompt:
      :wait: 1


wxpython
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b wxpython -f warning
      :prompt:
      :wait: 1


zenity
------------------------

.. program-screenshot:: python -m psidialogs.examples.demo -b zenity -f warning
      :prompt:
      :wait: 1

..  [[[end]]]

