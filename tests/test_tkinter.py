from test_dialogs import check
import pytest, psidialogs

@pytest.mark.parametrize("func", psidialogs.FUNCTION_NAMES)
def test_tkinter(func):
    check("tkinter", func)

