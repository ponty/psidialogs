import logging
import traceback

from psidialogs.childproc import childprocess_dialog
from psidialogs.err import FailedBackendError
from psidialogs.plugins.console_wrapper import ConsoleWrapper
from psidialogs.plugins.easygui_wrapper import EasyguiWrapper
from psidialogs.plugins.gmessage_wrapper import GmessageWrapper
from psidialogs.plugins.pyqt5_wrapper import PyQt5Wrapper
from psidialogs.plugins.pyside2_wrapper import PySide2Wrapper
from psidialogs.plugins.pythondialog_wrapper import PythonDialogWrapper
from psidialogs.plugins.tkinter_wrapper import TkinterWrapper
from psidialogs.plugins.wxpython_wrapper import WxPythonWrapper
from psidialogs.plugins.zenity_wrapper import ZenityWrapper

log = logging.getLogger(__name__)


backend_dict = {
    # TODO: ConsoleWrapper.name: ConsoleWrapper,
    # TODO: EasyguiWrapper.name: EasyguiWrapper,
    # TODO: GmessageWrapper.name: GmessageWrapper,
    # TODO: PyQt5Wrapper.name: PyQt5Wrapper,
    PySide2Wrapper.name: PySide2Wrapper,
    # TODO: PythonDialogWrapper.name: PythonDialogWrapper,
    TkinterWrapper.name: TkinterWrapper,
    # TODO: WxPythonWrapper.name: WxPythonWrapper,
    ZenityWrapper.name: ZenityWrapper,
}


def backends():
    yield PyQt5Wrapper
    yield PySide2Wrapper
    yield WxPythonWrapper
    yield EasyguiWrapper
    yield ZenityWrapper
    yield TkinterWrapper
    yield GmessageWrapper
    yield PythonDialogWrapper

    yield ConsoleWrapper

    # TODO: optimize order for platform
    # if platform_is_linux():
    # elif platform_is_osx():
    # elif platform_is_win():
    # else:


def select_childprocess(childprocess, backend_class):
    if backend_class.is_subprocess:
        # backend is always a subprocess -> nothing to do
        return False

    return childprocess


def dlg_dispatch(obj, dialogtype, argdict):
    if dialogtype == "message":
        return obj.message(argdict)
    elif dialogtype == "warning":
        return obj.warning(argdict)
    elif dialogtype == "error":
        return obj.error(argdict)
    elif dialogtype == "ask_ok_cancel":
        return obj.ask_ok_cancel(argdict)
    elif dialogtype == "ask_yes_no":
        return obj.ask_yes_no(argdict)
    elif dialogtype == "ask_string":
        return obj.ask_string(argdict)
    elif dialogtype == "ask_file":
        return obj.ask_file(argdict)
    elif dialogtype == "ask_folder":
        return obj.ask_folder(argdict)
    elif dialogtype == "choice":
        return obj.choice(argdict)
    # elif dialogtype == "multi_choice":
    #     return obj.multi_choice(argdict)


def auto(dialogtype, argdict, childprocess):
    for backend_class in backends():
        backend_name = backend_class.name
        log.debug("next backend to try: %s", backend_name)
        try:
            if select_childprocess(childprocess, backend_class):
                log.debug('running "%s" in child process', backend_name)
                return childprocess_dialog(dialogtype, backend_name, argdict)
            else:
                obj = backend_class()
                return dlg_dispatch(obj, dialogtype, argdict)
            break
        except Exception:
            msg = traceback.format_exc()
            log.debug(msg)

    msg = "All backends failed!"
    raise FailedBackendError(msg)


def force(backend_name, dialogtype, argdict, childprocess):
    backend_class = backend_dict[backend_name]
    if select_childprocess(childprocess, backend_class):
        log.debug('running "%s" in child process', backend_name)
        return childprocess_dialog(dialogtype, backend_name, argdict)
    else:
        obj = backend_class()
        return dlg_dispatch(obj, dialogtype, argdict)


def _opendialog(dialogtype, argdict, backend_name=None, childprocess=True):
    # TODO: check
    for (k, v) in argdict.items():
        if v is None:
            argdict[k] = ""
    log.debug(
        "_opendialog dialogtype:%s argdict:%s backend:%s childprocess:%s",
        dialogtype,
        argdict,
        backend_name,
        childprocess,
    )

    if backend_name:
        return force(backend_name, dialogtype, argdict, childprocess)
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
