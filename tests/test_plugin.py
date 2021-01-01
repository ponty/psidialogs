from pyvirtualdisplay.display import Display

from psidialogs.backendloader import BackendLoader


def test_pref():
    with Display(visible=0, size=(800, 600)) as vd:

        # TODO
        # BackendLoader().set_preference(["pygtk", "zenity"])
        # eq_(BackendLoader().selected().name, "pygtk")

        # BackendLoader().set_preference(["pygtk", "zenity", "pygtk"])
        # eq_(BackendLoader().selected().name, "pygtk")

        # BackendLoader().set_preference(["pygtk"])
        # eq_(BackendLoader().selected().name, "pygtk")

        # BackendLoader().set_preference(["zenity", "pygtk"])
        # eq_(BackendLoader().selected().name, "zenity")

        # BackendLoader().set_preference(["zenity", "pygtk", "zenity"])
        # eq_(BackendLoader().selected().name, "zenity")

        BackendLoader().set_preference(["zenity"])
        assert BackendLoader().selected().name == "zenity"


def test_force():
    with Display(visible=0, size=(800, 600)) as vd:
        for name in ["zenity"]:
            BackendLoader().force(name)
            assert BackendLoader().selected().name == name
            BackendLoader().force(None)
