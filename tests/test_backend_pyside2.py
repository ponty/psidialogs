import pytest
from check_dialog import check_dialog

import psidialogs

backend = "pyside2"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("PySide2.QtWidgets"):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_pyside2(dialogtype):
            check_dialog(backend, dialogtype)
