from test_dialogs import check_backend

from psidialogs.util import check_import

if check_import("PyQt5"):

    def test_pyqt5():
        check_backend("pyqt5")
