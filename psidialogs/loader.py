import logging
import multiprocessing
import traceback
from collections import OrderedDict
from threading import Lock

import psidialogs
from psidialogs.err import FailedBackendError
from psidialogs.plugins.easygui_wrapper import EasyguiWrapper
from psidialogs.plugins.gmessage_wrapper import GmessageWrapper
from psidialogs.plugins.pyqt5_wrapper import PyQt5Wrapper
from psidialogs.plugins.pyside2_wrapper import PySide2Wrapper
from psidialogs.plugins.tkinter_wrapper import TkinterWrapper
from psidialogs.plugins.pywin32_wrapper import Pywin32Wrapper
from psidialogs.plugins.wxpython_wrapper import WxPythonWrapper
from psidialogs.plugins.zenity_wrapper import ZenityWrapper
from psidialogs.util import platform_is_linux, platform_is_osx,platform_is_win

log = logging.getLogger(__name__)

# default preference order
# TODO:  PythonDialogWrapper,
# TODO:  ConsoleWrapper,
if platform_is_osx():
    backend_class_list = [
        WxPythonWrapper,
        PyQt5Wrapper,
        # PySide2Wrapper,
        # EasyguiWrapper,
        TkinterWrapper,
    ]
elif platform_is_win():
    backend_class_list = [
        Pywin32Wrapper,
        WxPythonWrapper,
        PyQt5Wrapper,
        # PySide2Wrapper,
        # EasyguiWrapper,
        TkinterWrapper,
    ]
else:
    backend_class_list = [
        WxPythonWrapper,
        PyQt5Wrapper,
        # PySide2Wrapper,
        # EasyguiWrapper,
        TkinterWrapper,
        ZenityWrapper,
        # GmessageWrapper,
    ]

backend_dict = OrderedDict([(b.name, b) for b in backend_class_list])

_preference = list(backend_dict.keys())


mutex = Lock()


def backend_preference():
    return _preference


def set_backend_preference(preference, disable_others):
    mutex.acquire()
    try:
        # log.debug("set_backend_preference: %s", preference)
        global _preference
        _preference = []
        keys = list(backend_dict.keys())
        if preference is None or preference == []:
            if disable_others:
                _preference = []
            else:
                _preference = keys
            return
        for b in preference:
            if b not in keys:
                log.error("unknown backend: %s", b)
                continue
            _preference.append(b)
            keys.remove(b)
        if not disable_others:
            _preference.extend(keys)
    finally:
        mutex.release()


# _force_backend = None


def select_childprocess(backend_class):
    if not psidialogs._ENABLE_CHILDPROCESS:
        return False
    if backend_class.is_subprocess:
        # backend is always a subprocess -> nothing to do
        return False
    return backend_class.need_subprocess


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


def auto(dialogtype, argdict):
    # if childprocess:
    #     log.debug('running "auto" in child process')
    #     return childprocess_dialog(dialogtype, argdict, preference=_preference)
    # else:
    for backend in _preference:
        # backend_class = backend_dict[backend]
        log.debug("next backend to try: %s", backend)
        try:
            # obj = backend_class()
            # return dlg_dispatch(obj, dialogtype, argdict)
            return force(backend, dialogtype, argdict)
        except Exception:
            msg = traceback.format_exc()
            log.debug(msg)

    msg = "All backends in preference failed!" + str(_preference)
    raise FailedBackendError(msg)


def ff(q, backend, dialogtype, argdict):
    backend_class = backend_dict[backend]
    obj = backend_class()
    ret = dlg_dispatch(obj, dialogtype, argdict)
    q.put(ret)


def force(backend, dialogtype, argdict):
    backend_class = backend_dict[backend]
    if select_childprocess(backend_class):
        log.debug('running "%s" in child process', backend)
        # return childprocess_dialog(dialogtype, argdict, backend=backend)
        q = multiprocessing.Queue()
        t = multiprocessing.Process(
            target=ff,
            args=(q, backend, dialogtype, argdict)
            # lambda: psidialogs.dialog(dialogtype, choices=["a", "b"])
        )
        t.start()
        result = q.get()
        t.join()
        return result
    else:
        obj = backend_class()
        return dlg_dispatch(obj, dialogtype, argdict)


def _opendialog(dialogtype, argdict):
    # TODO: check
    for (k, v) in argdict.items():
        if v is None:
            argdict[k] = ""
    log.debug(
        "_opendialog dialogtype:%s argdict:%s",
        dialogtype,
        argdict,
    )

    # if _force_backend:
    #     return force(_force_backend, dialogtype, argdict)
    # else:
    return auto(dialogtype, argdict)


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
