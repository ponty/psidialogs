API
===

..  [[[cog
..  cog.outl('' )
..  import psidialogs
..  functions=psidialogs.FUNCTION_NAMES
..  for f in functions:
..      cog.outl('' )
..      cog.outl(f + '()' )
..      cog.outl('------------------' )
..      cog.outl('' )
..      cog.outl('..' ) # extra comment, otherwise side TOC is bad
..      cog.outl('' )
..      cog.outl('.. automodule:: psidialogs' )
..      cog.outl('        :members: ' + f )
..      cog.outl('' )
..  cog.outl('' )
..  ]]]


ask_file()
------------------

..

.. automodule:: psidialogs
        :members: ask_file


ask_folder()
------------------

..

.. automodule:: psidialogs
        :members: ask_folder


ask_ok_cancel()
------------------

..

.. automodule:: psidialogs
        :members: ask_ok_cancel


ask_string()
------------------

..

.. automodule:: psidialogs
        :members: ask_string


ask_yes_no()
------------------

..

.. automodule:: psidialogs
        :members: ask_yes_no


choice()
------------------

..

.. automodule:: psidialogs
        :members: choice


error()
------------------

..

.. automodule:: psidialogs
        :members: error


message()
------------------

..

.. automodule:: psidialogs
        :members: message


multi_choice()
------------------

..

.. automodule:: psidialogs
        :members: multi_choice


text()
------------------

..

.. automodule:: psidialogs
        :members: text


warning()
------------------

..

.. automodule:: psidialogs
        :members: warning


..  [[[end]]]




