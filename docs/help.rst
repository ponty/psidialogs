command line help
==================================

..  [[[cog
..  import pcdialogs
..  ls='demo'.split()
..  for x in ls:
..      cog.outl('')
..      cog.outl('%s\n---------' % x)
..      cog.outl('')
..      cog.outl('.. program-output:: python -m pcdialogs.demo.%s --help'  % x)
..      cog.outl('      :prompt:')
..      cog.outl('')
..  ]]]

demo
---------

.. program-output:: python -m pcdialogs.demo.demo --help
      :prompt:

..  [[[end]]]

