import pytest

import psidialogs
from test_dialogs import check

backend = "tkinter"
if backend in psidialogs.backends():
    if psidialogs.util.check_import(backend):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_tkinter(dialogtype):
            check(backend, dialogtype)
