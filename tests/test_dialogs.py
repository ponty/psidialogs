from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from easyprocess import EasyProcess
from nose.tools import with_setup, eq_
from psidialogs.backendloader import BackendLoader
from pyvirtualdisplay.smartdisplay import SmartDisplay
import psidialogs

VISIBLE=0
screen = None
TIMEOUT=30

def check_buttons(cmd, expect):
    with EasyProcess(cmd):
#        time.sleep(1)
        screen.waitgrab(timeout=TIMEOUT)
        buttons = discover_buttons()

    eq_(len(buttons), len(expect), 
        msg='dialog does not have expected buttons %s!=%s' % (buttons,expect))
    
    mouse = PyMouse()
    print 'buttons:',buttons
    for v, b in zip(expect, buttons):
        process = EasyProcess(cmd).start().sleep(1)
        mouse.click(*b.center)
        process.wait()
        eq_(process.stdout, str(v)) #dialog does not return expected value

def check_open(cmd):
    # exception if nothing is displayed
    with EasyProcess(cmd):
        screen.waitgrab(timeout=TIMEOUT)
    

def check(backend, func):
    cmd = 'python -m psidialogs.examples.opendialog {backend} {func} -m hi'.format(backend=backend, func=func)
    check_open(cmd)
    
    if backend == 'pyqt':  # test not working, buttons are not active
        return
    if backend == 'wxpython' and func != 'message':  # wrong button taborder
        return
    if backend == 'easydialogs':
        if func in ['ask_ok_cancel','ask_yes_no']: 
            # can not hide button in easydialogs-gtk   
            return
    if backend == 'zenity':
        if func in ['ask_ok_cancel','ask_yes_no']: 
            # tab is not working in xvfb and xephyr   
            return
    if backend == 'gmessage':  # active editbox
        return
    
    if func == 'message':
        expect = [None]
        check_buttons(cmd, expect)
    if func == 'ask_yes_no':
        expect = [True, False]
        check_buttons(cmd, expect)
    if func == 'ask_ok_cancel':
        expect = [True, False]
        check_buttons(cmd, expect)

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
 
