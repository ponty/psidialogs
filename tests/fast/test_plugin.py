from nose.tools import eq_
from psidialogs.backendloader import BackendLoader
from unittest import TestCase


class Test(TestCase):
#        self.assertEquals(get_plugin(backend_preference=[]).name, 'pygtk')
#        self.assertEquals(get_plugin(backend_preference=[]).name, '')
#        self.assertEquals(get_plugin(backend_preference=['pygtk']).name, 'pygtk')
#        self.assertEquals(get_plugin(backend_preference=[]).name, 'zenity')
#        self.assertEquals(get_plugin(backend_preference=[]).name, 'zenity')
    def test_pref(self):
        BackendLoader().set_preference(['pygtk', 'zenity'])
        eq_(BackendLoader().selected().name, 'pygtk')

        BackendLoader().set_preference(['pygtk','zenity', 'pygtk'])
        eq_(BackendLoader().selected().name, 'pygtk')

        BackendLoader().set_preference(['pygtk'])
        eq_(BackendLoader().selected().name, 'pygtk')

        BackendLoader().set_preference(['zenity', 'pygtk'])
        eq_(BackendLoader().selected().name, 'zenity')

        BackendLoader().set_preference(['zenity','pygtk', 'zenity'])
        eq_(BackendLoader().selected().name, 'zenity')

        BackendLoader().set_preference(['zenity'])
        eq_(BackendLoader().selected().name, 'zenity')
        
    def test_force(self):
        for name in ['zenity', 'pygtk']:
            BackendLoader().force(name)
            eq_(BackendLoader().selected().name, name)
            BackendLoader().force(None)
        
       
        
        
        
        
        
        
        
