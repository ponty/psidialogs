import pytest

import psidialogs
from test_dialogs import check

backend = "pyqt5"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("PyQt5"):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_pyqt5(dialogtype):
            check(backend, dialogtype)
