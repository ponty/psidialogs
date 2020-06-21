from test_dialogs import check_backend
from psidialogs.util import check_import

if check_import("easygui"):

    def test_easygui():
        check_backend("easygui")
