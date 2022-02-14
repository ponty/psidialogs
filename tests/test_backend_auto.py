import pytest
from check_dialog import check_dialog

import psidialogs

backend = None


@pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
@pytest.mark.timeout(600)
def test_auto(dialogtype):
    check_dialog(backend, dialogtype)
