import pytest

import psidialogs
from test_dialogs import check

backend = "zenity"
if backend in psidialogs.backends():

    if psidialogs.util.prog_check(["zenity", "--help"]):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_zenity(dialogtype):
            check(backend, dialogtype)
