import pytest
from check_dialog import check_dialog

import psidialogs

backend = "pyqt5"
if psidialogs.util.backend_available(backend):

    @pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
    @pytest.mark.timeout(600)
    def test_pyqt5(dialogtype):
        check_dialog(backend, dialogtype)
