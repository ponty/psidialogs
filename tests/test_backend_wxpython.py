import pytest
from test_dialogs import check

import psidialogs

backend = "wxpython"
if backend in psidialogs.backends():

    if psidialogs.util.check_import("wx"):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_wxpython(dialogtype):
            check(backend, dialogtype)
