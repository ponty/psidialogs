import pytest
from check_dialog import check_dialog

import psidialogs

backend = "easygui"
if backend in psidialogs.backends():
    if psidialogs.util.check_import(backend):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_easygui(dialogtype):
            check_dialog(backend, dialogtype)
