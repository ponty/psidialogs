import pytest
from test_dialogs import check

import psidialogs

backend = "tkinter"
if backend in psidialogs.backends():
    if psidialogs.util.check_import(backend):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_tkinter(dialogtype):
            check(backend, dialogtype)
