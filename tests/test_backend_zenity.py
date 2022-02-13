import pytest
from test_dialogs import check

import psidialogs

backend = "zenity"
if backend in psidialogs.backends():

    if psidialogs.util.prog_check(["zenity", "--help"]):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_zenity(dialogtype):
            check(backend, dialogtype)
