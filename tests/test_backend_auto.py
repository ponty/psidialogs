import pytest

import psidialogs
from test_dialogs import check

backend = None


@pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
def test_auto(dialogtype):
    check(backend, dialogtype)
