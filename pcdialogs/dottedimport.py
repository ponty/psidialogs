import string
def dottedimport(name):
    # version of __import__ which handles dotted names
    # copied from python docs for __import__
    mod = __import__(name, globals(), locals(), [])
    components = string.split(name, '.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
