import psidialogs,logging

# from  psidialogs import loader


def test_force_backend():
    assert psidialogs.loader._force_backend is None

    psidialogs.force_backend("missing")
    assert psidialogs.loader._force_backend is None

    psidialogs.force_backend("tkinter")
    assert psidialogs.loader._force_backend == "tkinter"

    psidialogs.force_backend("missing")
    assert psidialogs.loader._force_backend == "tkinter"


def test_set_backend_preference():
    ls = psidialogs.backends()
    def pref():
        p= psidialogs.loader._preference
        logging.info('pref: %s',p)
        return p

    assert pref() == ls
    
    psidialogs.set_backend_preference([])
    assert pref() == ls

    psidialogs.set_backend_preference(["missing"])
    assert pref() == ls

    psidialogs.set_backend_preference(["tkinter"])
    assert pref()[0] == "tkinter"
    assert len(pref()) == len(ls)

    psidialogs.set_backend_preference(["missing","missing","missing","missing","missing","missing","missing","tkinter"])
    assert pref()[0] == "tkinter"
    assert len(pref()) == len(ls)

    psidialogs.set_backend_preference(["tkinter","missing","missing","missing","missing"])
    assert pref()[0] == "tkinter"
    assert len(pref()) == len(ls)


