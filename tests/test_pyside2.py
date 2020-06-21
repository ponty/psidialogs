from test_dialogs import check_backend

from psidialogs.util import check_import

if check_import("PySide2.QtWidgets"):

    def test_pyside2():
        check_backend("pyside2")
