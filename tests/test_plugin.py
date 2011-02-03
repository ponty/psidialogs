from pcdialogs.plugin_loader import get_all_plugins, get_plugin
from unittest import TestCase


class Test(TestCase):
    def test_pref(self):
        self.assertEquals(get_plugin(backend_preference=['zenity', 'pygtk']).name, 'zenity')
        self.assertEquals(get_plugin(backend_preference=['pygtk', 'zenity']).name, 'pygtk')
        self.assertEquals(get_plugin(backend_preference=['zenity']).name, 'zenity')
        self.assertEquals(get_plugin(backend_preference=['pygtk']).name, 'pygtk')
        self.assertEquals(get_plugin(backend_preference=['pygtk','zenity', 'pygtk']).name, 'pygtk')
        self.assertEquals(get_plugin(backend_preference=['zenity','pygtk', 'zenity']).name, 'zenity')
        
    def test_force(self):
        for name in ['zenity', 'pygtk']:
            p = get_plugin(force_backend=name)
            self.assertEquals(p.name, name)
        
    def test_all(self):
        ls=get_all_plugins()
        self.assertEquals(len(ls), 9)
        
        
        
        
        
        
        
        
