import pytest

import psidialogs
from test_dialogs import check

backend = "zenity"
if backend in psidialogs.backends():

    if psidialogs.util.prog_check(["zenity", "--help"]):

        @pytest.mark.parametrize("func", psidialogs.dialog_types())
        def test_zenity(func):
            check(backend, func)
