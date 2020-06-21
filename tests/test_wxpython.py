from test_dialogs import check_backend
from psidialogs.util import check_import

if check_import("wx"):

    def test_wxpython():
        check_backend("wxpython")
