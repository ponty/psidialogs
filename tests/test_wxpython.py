import pytest

import psidialogs
from test_dialogs import check

backend = "wxpython"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("wx"):

        @pytest.mark.parametrize("func", psidialogs.dialog_types())
        def test_wxpython(func):
            check(backend, func)
