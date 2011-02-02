Screenshots
==================================

..  [[[cog
..  import pcdialogs
..  backends='easygui wxlibdialogs'.split()
..  functions=pcdialogs.function_names
..  for f in functions:
..    cog.outl('')
..    cog.outl('------------------------')
..    cog.outl(f)
..    cog.outl('------------------------')
..    cog.outl('')
..    for b in backends:
..      cog.outl('')
..      #cog.outl(b)
..      #cog.outl('------------------------')
..      #cog.outl('')
..      cog.outl('.. program-screenshot:: python -m pcdialogs.demo.demo -b %s -f %s'  % (b,f))
..      #cog.outl('      :prompt:')
..      #cog.outl('      :stdout:')
..      #cog.outl('      :stderr:')
..      cog.outl('      :wait: 1')
..      cog.outl('')
..  ]]]

------------------------
message
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f message
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f message
      :wait: 1


------------------------
ask_string
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f ask_string
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f ask_string
      :wait: 1


------------------------
ask_file
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f ask_file
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f ask_file
      :wait: 1


------------------------
ask_folder
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f ask_folder
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f ask_folder
      :wait: 1


------------------------
choice
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f choice
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f choice
      :wait: 1


------------------------
multi_choice
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f multi_choice
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f multi_choice
      :wait: 1


------------------------
text
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f text
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f text
      :wait: 1


------------------------
error
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f error
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f error
      :wait: 1


------------------------
warning
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f warning
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f warning
      :wait: 1


------------------------
ask_files
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f ask_files
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f ask_files
      :wait: 1


------------------------
ask_ok_cancel
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f ask_ok_cancel
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f ask_ok_cancel
      :wait: 1


------------------------
ask_yes_no
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f ask_yes_no
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f ask_yes_no
      :wait: 1


------------------------
button_choice
------------------------


.. program-screenshot:: python -m pcdialogs.demo.demo -b easygui -f button_choice
      :wait: 1


.. program-screenshot:: python -m pcdialogs.demo.demo -b wxlibdialogs -f button_choice
      :wait: 1

..  [[[end]]]

