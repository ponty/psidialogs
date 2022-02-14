import pytest
from check_dialog import check_dialog

import psidialogs

backend = "zenity"
if backend in psidialogs.backends():

    if psidialogs.util.prog_check(["zenity", "--help"]):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_zenity(dialogtype):
            check_dialog(backend, dialogtype)
