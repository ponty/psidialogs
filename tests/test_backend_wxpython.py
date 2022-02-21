import pytest
from check_dialog import check_dialog

import psidialogs

backend = "wxpython"
if psidialogs.util.backend_available(backend):

    @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
    @pytest.mark.timeout(600)
    def test_wxpython(dialogtype):
        check_dialog(backend, dialogtype)
