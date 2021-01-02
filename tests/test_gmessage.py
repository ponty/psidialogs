import pytest

import psidialogs
from test_dialogs import check

backend = "gmessage"
if backend in psidialogs.backends():
    if psidialogs.util.prog_check(["gmessage", "-h"]):

        @pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
        def test_gmessage(func):
            check(backend, func)
