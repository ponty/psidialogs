import pytest
from test_dialogs import check

import psidialogs

backend = "pyside2"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("PySide2.QtWidgets"):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_pyside2(dialogtype):
            check(backend, dialogtype)
