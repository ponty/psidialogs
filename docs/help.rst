command line help
==================================

..  [[[cog
..  import psidialogs
..  ls='demo'.split()
..  for x in ls:
..      cog.outl('')
..      cog.outl('%s\n---------' % x)
..      cog.outl('')
..      cog.outl('.. program-output:: python -m psidialogs.examples.%s --help'  % x)
..      cog.outl('      :prompt:')
..      cog.outl('')
..  ]]]

demo
---------

.. program-output:: python -m psidialogs.examples.demo --help
      :prompt:

..  [[[end]]]

