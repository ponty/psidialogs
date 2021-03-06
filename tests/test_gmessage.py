import pytest

import psidialogs
from test_dialogs import check

backend = "gmessage"
if backend in psidialogs.backends():
    if psidialogs.util.prog_check(["gmessage", "-h"]):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        def test_gmessage(dialogtype):
            check(backend, dialogtype)
