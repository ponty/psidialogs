import logging
import traceback

from psidialogs.childproc import childprocess_dialog
from psidialogs.err import FailedBackendError
from psidialogs.plugins.pyside2_wrapper import PySide2Wrapper
from psidialogs.plugins.tkinter_wrapper import TkinterWrapper
from psidialogs.plugins.zenity_wrapper import ZenityWrapper

log = logging.getLogger(__name__)

# default preference order
backend_class_list = [
    # TODO:  PyQt5Wrapper,
    PySide2Wrapper,
    # TODO:  WxPythonWrapper,
    # TODO:  EasyguiWrapper,
    TkinterWrapper,
    ZenityWrapper,
    # TODO:  GmessageWrapper,
    # TODO:  PythonDialogWrapper,
    # TODO:  ConsoleWrapper,
]
backend_dict = dict([(b.name, b) for b in backend_class_list])

_preference = [b.name for b in backend_class_list]


def set_backend_preference(preference):
    log.debug("set_backend_preference: %s", preference)
    global _preference
    _preference = []
    keys = list(backend_dict.keys())
    for b in preference:
        if b not in keys:
            log.error("unknown backend: %s", b)
            continue
        _preference.append(b)
        keys.remove(b)
    _preference.extend(keys)


_force_backend = None


def force_backend(b):
    log.debug("force_backend %s", b)
    global _force_backend
    if b is None:
        _force_backend = b
    elif b in backend_dict.keys():
        _force_backend = b
    else:
        log.error("unknown backend: %s", b)


# def backends():
#     yield PyQt5Wrapper
#     yield PySide2Wrapper
#     yield WxPythonWrapper
#     yield EasyguiWrapper
#     yield ZenityWrapper
#     yield TkinterWrapper
#     yield GmessageWrapper
#     yield PythonDialogWrapper
#     yield ConsoleWrapper


def select_childprocess(childprocess, backend_class):
    if backend_class.is_subprocess:
        # backend is always a subprocess -> nothing to do
        return False

    return childprocess


def dlg_dispatch(obj, dialogtype, argdict):
    message = argdict["message"]
    title = argdict["title"]
    if dialogtype == "message":
        return obj.message(message, title)
    elif dialogtype == "warning":
        return obj.warning(message, title)
    elif dialogtype == "error":
        return obj.error(message, title)
    elif dialogtype == "ask_ok_cancel":
        return obj.ask_ok_cancel(message, title)
    elif dialogtype == "ask_yes_no":
        return obj.ask_yes_no(message, title)
    elif dialogtype == "ask_string":
        return obj.ask_string(message, title)
    elif dialogtype == "ask_file":
        return obj.ask_file(message, title)
    elif dialogtype == "ask_folder":
        return obj.ask_folder(message, title)
    elif dialogtype == "choice":
        choices = argdict["choices"]
        return obj.choice(choices, message, title)
    # elif dialogtype == "multi_choice":
    #     return obj.multi_choice(argdict)


def auto(dialogtype, argdict, childprocess):
    if childprocess:
        log.debug('running "auto" in child process')
        return childprocess_dialog(dialogtype, argdict, preference=_preference)
    else:
        for backend_class in backend_class_list:
            backend = backend_class.name
            log.debug("next backend to try: %s", backend)
            try:
                obj = backend_class()
                return dlg_dispatch(obj, dialogtype, argdict)
            except Exception:
                msg = traceback.format_exc()
                log.debug(msg)

        msg = "All backends failed!"
        raise FailedBackendError(msg)


def force(backend, dialogtype, argdict, childprocess):
    backend_class = backend_dict[backend]
    if select_childprocess(childprocess, backend_class):
        log.debug('running "%s" in child process', backend)
        return childprocess_dialog(dialogtype, argdict, backend=backend)
    else:
        obj = backend_class()
        return dlg_dispatch(obj, dialogtype, argdict)


def _opendialog(dialogtype, argdict, childprocess=True):
    # TODO: check
    for (k, v) in argdict.items():
        if v is None:
            argdict[k] = ""
    log.debug(
        "_opendialog dialogtype:%s argdict:%s childprocess:%s",
        dialogtype,
        argdict,
        childprocess,
    )

    if _force_backend:
        return force(_force_backend, dialogtype, argdict, childprocess)
    else:
        return auto(dialogtype, argdict, childprocess)


def backend_version2(backend_name):
    backend_class = backend_dict[backend_name]
    obj = backend_class()
    v = obj.backend_version()
    return v


# class PluginLoaderError(Exception):
#     pass


# class PluginLoader(object):
#     def __init__(self, default_preference=[]):
#         self.plugins = dict()

#         self.all_names = [x.name for x in IPlugin.__subclasses__()]

#         self.changed = True
#         self._force_backend = None
#         self.preference = []
#         self.default_preference = default_preference
#         self._backend = None

#     def set_preference(self, x):
#         self.changed = True
#         self.preference = x

#     def force(self, name):
#         log.debug("forcing:" + str(name))
#         self.changed = True
#         self._force_backend = name

#     @property
#     def is_forced(self):
#         return self._force_backend is not None

#     @property
#     def loaded_plugins(self):
#         return self.plugins.values()

#     def get_valid_plugin_by_name(self, name):
#         if name not in self.plugins:
#             ls = filter(lambda x: x.name == name, IPlugin.__subclasses__())
#             ls = list(ls)
#             if len(ls):
#                 try:
#                     plugin = ls[0]()
#                 except Exception as e:
#                     log.debug("%s exception: %s", ls[0].name, e)
#                     plugin = None
#             else:
#                 plugin = None
#             self.plugins[name] = plugin
#         return self.plugins[name]

#     def get_valid_plugin_by_list(self, ls):
#         for name in ls:
#             x = self.get_valid_plugin_by_name(name)
#             if x:
#                 return x

#     def selected(self):
#         if self.changed:
#             if self.is_forced:
#                 b = self.get_valid_plugin_by_name(self._force_backend)
#                 if not b:
#                     raise PluginLoaderError(
#                         "Forced backend not found, or cannot be loaded:"
#                         + self._force_backend
#                     )
#             else:
#                 biglist = self.preference + self.default_preference + self.all_names
#                 b = self.get_valid_plugin_by_list(biglist)
#                 if not b:
#                     self.raise_exc()
#             self.changed = False
#             self._backend = b
#             log.debug("selecting plugin:" + self._backend.name)
#         return self._backend

#     def raise_exc(self):
#         message = "Install at least one backend!"
#         raise PluginLoaderError(message)
