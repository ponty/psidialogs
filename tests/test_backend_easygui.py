import pytest
from test_dialogs import check

import psidialogs

backend = "easygui"
if backend in psidialogs.backends():
    if psidialogs.util.check_import(backend):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_easygui(dialogtype):
            check(backend, dialogtype)
