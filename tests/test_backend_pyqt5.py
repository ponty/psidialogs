import pytest
from test_dialogs import check

import psidialogs

backend = "pyqt5"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("PyQt5"):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_pyqt5(dialogtype):
            check(backend, dialogtype)
