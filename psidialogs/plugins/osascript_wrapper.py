from psidialogs.iplugin import IPlugin
from psidialogs.util import platform_is_osx
import logging
import os
import distutils.sysconfig
import ctypes

log = logging.getLogger(__name__)


class OsascriptWrapper(IPlugin):
    name = "osascript"
    is_subprocess = True

    def backend_version(self):
        return extract_version(EasyProcess(["osascript", "--version"]).call().stdout)

    def _call(self, message, title, options, useReturnCode=0):
        if title:
            options["-name"] = title
        options["-center"] = None

        def dict2list(d):
            ls = []
            for k, v in d.items():
                if k:
                    ls.append(k)
                if v:
                    ls.append(v)
            return ls

        cmd = ["osascript", message] + dict2list(options)
        p = EasyProcess(cmd).call()
        if useReturnCode:
            return p.return_code
        result = p.stdout.strip()
        if not result:
            result = None
        return result

    # def ask_string(self, message, title):

    def message(self, message, title):
        # osascript -e 'display dialog "Hello from osxdaily.com" with title "Hello"'
        cmd = ["osascript",'-e', message] + dict2list(options)
        p = EasyProcess(cmd).call()

        # options = {}
        # options["--%s" % kw] = None
        # options["--text"] = message
        # return self._call(title, options)

    # def error(self, message, title):

    # def warning(self, message, title):

    # def ask_ok_cancel(self, message, title):

    # def ask_yes_no(self, message, title):

    # def ask_file(self, message, title):

    # def ask_folder(self, message, title):

    # def choice(self, choices, message, title):
