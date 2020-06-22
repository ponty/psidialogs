from test_dialogs import check_backend
from psidialogs.util import check_import
from test_dialogs import check
import pytest, psidialogs

if check_import("easygui"):

    @pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
    def test_easygui(func):
        check("easygui", func)
