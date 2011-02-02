Screenshots
==================================

..  [[[cog
..  import pcdialogs
..  backends='easygui wxlibdialogs tk'.split()
..  functions='message warning error'.split()
..  for f in functions:
..    cog.outl('')
..    cog.outl('---------')
..    cog.outl(f)
..    cog.outl('---------')
..    cog.outl('')
..    for b in backends:
..      cog.outl('')
..      cog.outl(b)
..      cog.outl('---------')
..      cog.outl('')
..      cog.outl('.. program-screenshot:: python -m pcdialogs.demo.demo -b %s -f %s'  % (b,f))
..      cog.outl('      :prompt:')
..      cog.outl('      :stdout:')
..      cog.outl('      :stderr:')
..      cog.outl('      :wait: 1')
..      cog.outl('')
..  ]]]

---------
message
---------


easygui
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f message
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


wxlibdialogs
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f message
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


tk
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b tk -f message
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


---------
warning
---------


easygui
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f warning
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


wxlibdialogs
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f warning
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


tk
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b tk -f warning
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


---------
error
---------


easygui
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f error
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


wxlibdialogs
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f error
      :prompt:
      :stdout:
      :stderr:
      :wait: 1


tk
---------

.. program-screenshot:: python -m pcdialogs.demo.demo -b tk -f error
      :prompt:
      :stdout:
      :stderr:
      :wait: 1

..  [[[end]]]

