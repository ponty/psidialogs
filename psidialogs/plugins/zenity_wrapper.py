from easyprocess import EasyProcess

from psidialogs.iplugin import IPlugin
from psidialogs.util import extract_version


class ZenityWrapper(IPlugin):
    name = "zenity"
    is_subprocess = True

    def backend_version(self):
        return extract_version(EasyProcess(["zenity", "--version"]).call().stdout)

    def _call(self, title, options, useReturnCode=False, extraargs=[]):
        if title:
            options["--title"] = title

        def dict2list(d):
            ls = []
            for k, v in d.items():
                if k:
                    ls += [k]
                if v is not None:
                    ls += [v]
            return ls

        # print ['zenity']  , dict2list(options) , extraargs
        cmd = ["zenity"] + dict2list(options) + extraargs
        p = EasyProcess(cmd).call()
        if useReturnCode:
            return p.return_code
        result = p.stdout.strip()
        if not result:
            result = None
        return result

    def _message(self, message, title, kw):
        options = {}
        options["--%s" % kw] = None
        options["--text"] = message
        return self._call(title, options)

    # def text(self, args):
    #     options = {}
    #     f = tempfile.NamedTemporaryFile()
    #     f.write(uniencode(args["text"]))
    #     f.flush()
    #     options["--text-info"] = None
    #     options["--filename"] = f.name
    #     result = self._call(args, options)
    #     f.close()
    #     return result

    def message(self, message, title):
        return self._message(message, title, "info")

    def warning(self, message, title):
        return self._message(message, title, "warning")

    def error(self, message, title):
        return self._message(message, title, "error")

    def _entry(self, message, title, pw):
        options = {}
        options["--entry"] = None
        options["--text"] = message
        if pw:
            options["--hide-text"] = None
        # if args["default"]:
        #     options["--entry-text"] = args["default"]
        return self._call(title, options)

    def ask_string(self, message, title):
        return self._entry(message, title, pw=0)

    def _file(self, message, title, multi, folder):
        options = {}
        separator = "|"
        options["--file-selection"] = None
        options["--text"] = message
        if multi:
            options["--multiple"] = None
            options["--separator"] = separator
        if folder:
            options["--directory"] = None
        # if args["default"]:
        #     options["--filename"] = args["default"]
        result = self._call(title, options)
        if result and multi:
            result = result.split(separator)
        return result

    def _choice(self, choices, message, title, multi):
        options = {}
        separator = "|"
        options["--list"] = None
        options["--text"] = message
        if multi:
            options["--multiple"] = None
            options["--checklist"] = None
            options["--separator"] = separator

            extraargs = ["--column", "Select", "--column", "Item"]
            for x in choices:
                extraargs += ["FALSE", x]
        else:
            extraargs = ["--column", "Item"] + choices
        result = self._call(title, options, extraargs=extraargs)
        if result and multi:
            result = result.split(separator)
        return result

    def ask_file(self, message, title):
        return self._file(message, title, multi=0, folder=0)

    def ask_folder(self, message, title):
        return self._file(message, title, multi=0, folder=1)

    def _ask_question(self, message, title, ok, cancel):
        options = {}
        options["--question"] = None
        options["--text"] = message
        options["--ok-label"] = ok
        options["--cancel-label"] = cancel
        result = self._call(title, options, useReturnCode=1)
        result = not result
        return result

    def ask_ok_cancel(self, message, title):
        return self._ask_question(message, title, ok="OK", cancel="Cancel")

    def ask_yes_no(self, message, title):
        return self._ask_question(message, title, ok="Yes", cancel="No")

    def choice(self, choices, message, title):
        return self._choice(choices, message, title, multi=0)

    # def multi_choice(self, args):
    #     return self._choice(args, multi=1)
