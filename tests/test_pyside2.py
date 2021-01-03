import pytest

import psidialogs
from test_dialogs import check

backend = "pyside2"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("PySide2.QtWidgets"):

        @pytest.mark.parametrize("func", psidialogs.dialog_types())
        def test_pyside2(func):
            check(backend, func)
