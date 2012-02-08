from easyprocess import EasyProcess
from nose.tools import with_setup, eq_
from psidialogs.backendloader import BackendLoader
from pyvirtualdisplay.smartdisplay import SmartDisplay
import psidialogs


screen = None
VISIBLE=0

def check(backend, func):
    return
    cmd = 'python -m psidialogs.examples.unicode_demo -b {backend} -f {func}'.format(backend=backend, func=func)
    EasyProcess(cmd).wrap(screen.waitgrab)()
    
    

def setup_func():
    "set up test fixtures"
    global screen
    screen = SmartDisplay(visible=VISIBLE)
    screen.start()

def teardown_func():
    "tear down test fixtures"
    global screen
    screen.stop()

      
s = ''        
for x in BackendLoader().all_names:
    for f in psidialogs.FUNCTION_NAMES:
        if not BackendLoader().is_console(x):
            s += '''
@with_setup(setup_func, teardown_func)
def test_{backend}_{safefunc}():
    check("{backend}","{func}")
'''.format(backend=x, func=f, safefunc=f.replace('error','err').replace('warning','warn'))     
exec s

@with_setup(setup_func, teardown_func)
def dummy():
    pass   
 
