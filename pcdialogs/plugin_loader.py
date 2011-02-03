from yapsy.PluginManager import PluginManager
import logging
from path import path
import platform
#log=logging.getLogger(__name__)
log = logging

class MyPluginManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self)
        places = [path(__file__).dirname() / 'backends']
        ext = 'conf'
        self.setPluginInfoExtension(ext)
        self.setPluginPlaces(places)
        self.locatePlugins()
        self.loadPlugins()
        self.set_names()

    def getAllPlugins(self):
        all = PluginManager.getAllPlugins(self)
        all = [x.plugin_object for x in all] 
        return all

    def set_names(self):
        all = PluginManager.getAllPlugins(self)
        for x in all:
            x.plugin_object.name = x.name
         
    def activatePlugin(self, plugin_object):
        po = plugin_object
        if not hasattr(po, 'is_activated') or not po.is_activated:
            po.activate()
            po.is_activated = True
        
    def activatePluginByName(self, name):
        pi = self.getPluginByName(name)
        po = pi.plugin_object
        self.activatePlugin(po)
        return po

    def activatePlugins(self):
        all = self.getAllPlugins()
        for po in all:
            self.activatePlugin(po)

_PM = None
def get_plugin_manager():  
    global _PM
    if _PM:
        return _PM  

    pm = MyPluginManager()

    _PM = pm
    return pm

           
def get_plugin(backend_preference=None, force_backend=None):    
    pm = get_plugin_manager()
    
    if force_backend:
        return pm.activatePluginByName(force_backend)
    
    all = pm.getAllPlugins()

    if backend_preference:
        def key(x):
            if x.name in backend_preference:
                return backend_preference.index(x.name)
            return 1000
        
        log.debug('before sort:')
        log.debug([x.name for x in all])
        
        all.sort(key=key)
        
        log.debug('after sort:')
        log.debug([x.name for x in all])
    
    if len(all):
        # get first
        x = all[0]
        pm.activatePlugin(x)
        return x
    else:
        raise(Exception('no plugin found!'))
        
    
    message = 'Install at least one backend!' 
    for x in all:
        message += '\n'
        message += '[%s]' % (x.name)
        if hasattr(x, 'home_url'):
            home_url = x.home_url
            message += '\n'
            message += '%s' % (home_url)
        message += '\n'
        if platform.dist()[0].lower() == 'ubuntu':
            message += 'You can install it in terminal:'
            message += '\n'
            message += '\t'
            message += 'sudo apt-get install %s' % x.ubuntu_package
    raise Exception(message)


def get_all_plugins():    
    pm = get_plugin_manager()
    pm.activatePlugins()
    all = pm.getAllPlugins()
    
    return all
    
