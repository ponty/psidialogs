import pytest

import psidialogs
from psidialogs.util import check_import
from test_dialogs import check

if check_import("PySide2.QtWidgets"):

    @pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
    def test_pyside2(func):
        check("pyside2", func)
