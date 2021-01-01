import pytest

import psidialogs
from psidialogs.util import check_import
from test_dialogs import check

if check_import("PyQt5"):

    @pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
    def test_pyqt5(func):
        check("pyqt5", func)
