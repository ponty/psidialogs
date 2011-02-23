from UserDict import DictMixin
class attribdict(DictMixin):
    """
    >>> x = attribdict(a=1,b=2)
    >>> x
    {'a': 1, 'b': 2}
    >>> x.a
    1
    >>> x['b']
    2
    >>> x = attribdict(dict(c=1,d=2))
    >>> x.d
    2
    >>> x = attribdict({'c': 3 , 'd' : 4})
    >>> x.d
    4
    """
    def __init__(self, *args, **kwargs):
        self.__dict__ = ( dict(*args, **kwargs) )

    def __getitem__(self, key):
        return self.__dict__ [key]
    def keys(self):
        return self.__dict__ .keys()

    def copy(self):
        if self.__class__ is attribdict:
            return attribdict(self.__dict__.copy())
