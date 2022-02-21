import logging

import psidialogs


def pref():
    p = psidialogs.backend_preference()
    logging.info("pref: %s", p)
    return p


def test_set_backend_preference():
    psidialogs.set_backend_preference()
    ls = psidialogs.backends()
    logging.warning(f"ls {ls}")

    assert pref() == ls

    psidialogs.set_backend_preference([])
    assert pref() == ls

    logging.warning(f"ls {ls}")
    logging.warning(f"pref() {pref()}")
    psidialogs.set_backend_preference(["missing"])
    logging.warning(f"ls {ls}")
    logging.warning(f"pref() {pref()}")
    assert pref() == ls

    psidialogs.set_backend_preference(["tkinter"])
    assert pref()[0] == "tkinter"
    assert len(pref()) == len(ls)

    psidialogs.set_backend_preference(
        [
            "missing",
            "missing",
            "missing",
            "missing",
            "missing",
            "missing",
            "missing",
            "tkinter",
        ]
    )
    assert pref()[0] == "tkinter"
    assert len(pref()) == len(ls)

    psidialogs.set_backend_preference(
        ["tkinter", "missing", "missing", "missing", "missing"]
    )
    assert pref()[0] == "tkinter"
    assert len(pref()) == len(ls)


def test_set_backend_preference_disable_others():
    psidialogs.set_backend_preference()
    ls = psidialogs.backends()

    assert pref() == ls

    psidialogs.set_backend_preference([], disable_others=True)
    assert pref() == []

    psidialogs.set_backend_preference(["missing"], disable_others=True)
    assert pref() == []

    psidialogs.set_backend_preference(["tkinter"], disable_others=True)
    assert pref() == ["tkinter"]

    psidialogs.set_backend_preference(
        [
            "missing",
            "missing",
            "missing",
            "missing",
            "missing",
            "missing",
            "missing",
            "tkinter",
        ],
        disable_others=True,
    )
    assert pref() == ["tkinter"]

    psidialogs.set_backend_preference(
        ["tkinter", "missing", "missing", "missing", "missing"], disable_others=True
    )
    assert pref() == ["tkinter"]
