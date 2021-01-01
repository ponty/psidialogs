import pytest

import psidialogs
from psidialogs.util import check_import
from test_dialogs import check

if check_import("easygui"):

    @pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
    def test_easygui(func):
        check("easygui", func)
