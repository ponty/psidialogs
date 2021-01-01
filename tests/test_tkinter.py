import pytest

import psidialogs
from test_dialogs import check


@pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
def test_tkinter(func):
    check("tkinter", func)
