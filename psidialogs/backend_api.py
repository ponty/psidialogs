# TODO
# import logging

# from psidialogs.backendloader import BackendLoader
# from psidialogs.mixins import AllMixin

# log = logging.getLogger(__name__)


# def opendialog(funcname, argdict):
#     for (k, v) in argdict.items():
#         if v is None:
#             argdict[k] = ""

#     log.debug(funcname)
#     log.debug(argdict)
#     b = BackendLoader().selected()
#     f = b.__class__.__dict__.get(funcname)
#     if not f:
#         log.debug("backend method not found, using mixin")

#         class Backend(b.__class__, AllMixin):
#             pass

#         b = Backend()
#         f = AllMixin.__dict__.get(funcname)

#     return f(b, argdict)
