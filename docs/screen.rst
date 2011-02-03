Screenshots
==================================


..  [[[cog
..  import pcdialogs
..  backends=pcdialogs.all_backends()
..  functions=pcdialogs.FUNCTION_NAMES
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
..    cog.outl(':func:`API<pcdialogs.%s>`' % f)
..    cog.outl('')
..    for b in backends:
..      cog.outl('')
..      cog.outl(b.backend)
..      cog.outl('------------------------')
..      cog.outl('')
..      cmd = 'python -m pcdialogs.demo.demo -b %s -f %s'  % (b.name,f)
..      if hasattr(b,'console') and b.console:
..         cmd='xterm -e "%s"' % cmd
..      #cog.outl('.. program-screenshot:: ' + cmd )
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

:func:`API<pcdialogs.ask_ok_cancel>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _ask_string:

------------------------
ask_string()
------------------------

:func:`API<pcdialogs.ask_string>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _ask_yes_no:

------------------------
ask_yes_no()
------------------------

:func:`API<pcdialogs.ask_yes_no>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _button_choice:

------------------------
button_choice()
------------------------

:func:`API<pcdialogs.button_choice>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _choice:

------------------------
choice()
------------------------

:func:`API<pcdialogs.choice>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _error:

------------------------
error()
------------------------

:func:`API<pcdialogs.error>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _message:

------------------------
message()
------------------------

:func:`API<pcdialogs.message>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _multi_choice:

------------------------
multi_choice()
------------------------

:func:`API<pcdialogs.multi_choice>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _text:

------------------------
text()
------------------------

:func:`API<pcdialogs.text>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1


.. _warning:

------------------------
warning()
------------------------

:func:`API<pcdialogs.warning>`


Zenity
------------------------

      :prompt:
      :wait: 1


EasyGui
------------------------

      :prompt:
      :wait: 1


console
------------------------

      :prompt:
      :wait: 1


gMessage
------------------------

      :prompt:
      :wait: 1


TkInter
------------------------

      :prompt:
      :wait: 1


Python Dialog
------------------------

      :prompt:
      :wait: 1


wxPython
------------------------

      :prompt:
      :wait: 1


PyQt
------------------------

      :prompt:
      :wait: 1


PyGTK
------------------------

      :prompt:
      :wait: 1

..  [[[end]]]

