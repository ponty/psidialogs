import pytest

import psidialogs
from test_dialogs import check

backend = "easygui"
if backend in psidialogs.backends():
    if psidialogs.util.check_import(backend):

        @pytest.mark.parametrize("func", psidialogs.dialog_types())
        def test_easygui(func):
            check(backend, func)
