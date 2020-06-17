from nose.tools import eq_
from psidialogs.backendloader import BackendLoader
from unittest import TestCase
from pyvirtualdisplay.display import Display


class Test(TestCase):
    #        self.assertEquals(get_plugin(backend_preference=[]).name, 'pygtk')
    #        self.assertEquals(get_plugin(backend_preference=[]).name, '')
    #        self.assertEquals(get_plugin(backend_preference=['pygtk']).name, 'pygtk')
    #        self.assertEquals(get_plugin(backend_preference=[]).name, 'zenity')
    #        self.assertEquals(get_plugin(backend_preference=[]).name, 'zenity')
    def test_pref(self):
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
            eq_(BackendLoader().selected().name, "zenity")

    def test_force(self):
        with Display(visible=0, size=(800, 600)) as vd:
            for name in ["zenity"]:
                BackendLoader().force(name)
                eq_(BackendLoader().selected().name, name)
                BackendLoader().force(None)
