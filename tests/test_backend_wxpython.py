import pytest
from check_dialog import check_dialog

import psidialogs
from psidialogs.util import backend_available

backend = "wxpython"
if backend_available(backend):

    @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
    @pytest.mark.timeout(600)
    def test_wxpython(dialogtype):
        check_dialog(backend, dialogtype)
