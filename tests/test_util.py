from psidialogs.util import extract_version


def test_extract_version():
    assert extract_version("3.42.1") == "3.42.1"
