import pytest
from check_dialog import check_dialog

import psidialogs

backend = "gmessage"
if backend in psidialogs.backends():
    if psidialogs.util.prog_check(["gmessage", "-h"]):

        @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
        @pytest.mark.timeout(600)
        def test_gmessage(dialogtype):
            check_dialog(backend, dialogtype)
