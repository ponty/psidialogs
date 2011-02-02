##from functools import wraps
##from decorator import decorator
import inspect

def changeReturnValue(f, funcOnReturn):    
    '''
    >>> def f(x,y,z=7):      return x+y
    >>> f(1,2)
    3
    >>> f2 = changeReturnValue(f,lambda x:x*2)
    >>> f2(1,2)
    6
    '''
##    @wraps(f)
    def wrapper(*args, **kwargs):
        return funcOnReturn( f(*args, **kwargs) )
    return wrapper

def changeArg(f, **funcOnArgDict):
    '''
    >>> def f(x,y,z=7):       return x+y
    >>> f(1,2)
    3
    >>> f3 = changeArg(f,y = lambda x:x*2)
    >>> f3(y=2, x=1,)
    5
    >>> f3(1,2)
    5
    >>> f3(1,y=2)
    5
    '''
    regargs, _, _, _ = inspect.getargspec(f)
##    @wraps(f)
    def wrapper(*args, **kwargs):
        posargdict = dict(zip(regargs, args))
        def updateDict(d, argname, funcOnArg):
            if d.has_key(argname):
                d[argname] = funcOnArg(d[argname])
        for argname,funcOnArg in funcOnArgDict.items():
            updateDict(kwargs,      argname,funcOnArg)
            updateDict(posargdict, argname,funcOnArg)
        args = [ posargdict[x] for x, _ in zip(regargs, args) ]
        return f(*args, **kwargs)
    return wrapper

def returnNone(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
    return wrapper
    
    
if __name__ == "__main__":
    import doctest; doctest.testmod()

