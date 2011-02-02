

def filterNone(**d):
    for (k,v) in d.items():
        if k is None or v is None:
            del d[k]
    return d
