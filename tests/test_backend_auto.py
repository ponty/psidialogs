import pytest
from test_dialogs import check

import psidialogs

backend = None


@pytest.mark.parametrize("dialogtype", psidialogs.dialog_types())
@pytest.mark.timeout(600)
def test_auto(dialogtype):
    check(backend, dialogtype)
