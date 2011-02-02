import subprocess
import logging
import os,signal,time

def _create_args(executable, args=[], options={}):
    args = list(args)
    optionlist = []
    for (k,v) in options.items():
        optionlist += [ k]
        if v is not None:
            optionlist += [ v ]
    args = [executable] + optionlist + args
    args = map(str, args)
    return args 

def start(executable, args=[], options={}, quiet=False):
    args = _create_args(executable, args, options)
    p = subprocess.Popen( args = args,
                          stdout = subprocess.PIPE  if quiet else None,
                          stderr = subprocess.PIPE if quiet else None,
                          )
    return p

def kill(process):
    if process.poll() is None:
        logging.debug(  'process was killed' )
        os.kill(process.pid, signal.SIGKILL)
    return process.wait()
    
def call(executable, args=[], options={}, input = None, useReturnCode= True , timeout = None):
    """ 
    input     -- stdin
    return    -- stdout / returncode
    """ 
    
    if useReturnCode:
        args = _create_args(executable, args, options)
        logging.debug(args)
        p = subprocess.Popen( args = args,
                              stdin = subprocess.PIPE if input else None,
                              stdout = subprocess.PIPE if not useReturnCode else None,
                              stderr = subprocess.PIPE if not useReturnCode else None,
                              close_fds = True)
        if input is not None:
            raise NotImplementedError('input')
        if timeout is not None:
            polltime = 0.05
            for x in range(int(timeout/polltime)): 
                if p.poll() is not None:
                    logging.debug( 'run time:%d ms timeout:%d ms' % (int(1000*x*polltime), timeout*1000) )
                    break
                time.sleep(polltime)
            return kill(p)
        else:
            return p.wait()
    else:
        if timeout is not None:
            raise NotImplementedError('timeout')
        (out, err) = call_with_communicate(executable, args, options, input)
        return out

def call_with_communicate(executable, args=[], options={}, input = None):
    """ 
    input     -- stdin
    return    -- (stdout , stderr)
    """ 
    args = _create_args(executable, args, options)
    logging.debug(args)
    p = subprocess.Popen( args = args,
                          stdin = subprocess.PIPE if input else None,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE,
                          close_fds = True)
    stdout_text, stderr_text = p.communicate(input)
    return (stdout_text.rstrip(), stderr_text.rstrip() )
