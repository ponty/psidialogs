from easyprocess import EasyProcess

from psidialogs import mixins
from psidialogs.iplugin import IPlugin
from psidialogs.util import extract_version


class GmessageWrapper(IPlugin):
    name = "gmessage"
    is_subprocess = True

    def backend_version(self):
        return extract_version(EasyProcess(["gmessage", "--version"]).call().stdout)

    def _call(self, message, title, options, useReturnCode=0):
        if title:
            options["-name"] = title
        options["-center"] = None

        def dict2list(d):
            ls = []
            for k, v in d.items():
                if k:
                    ls += [k]
                if v:
                    ls += [v]
            return ls

        cmd = ["gmessage", message] + dict2list(options)
        p = EasyProcess(cmd).call()
        if useReturnCode:
            return p.return_code
        result = p.stdout.strip()
        if not result:
            result = None
        return result

    def message(self, message, title):
        options = {}
        options["-buttons"] = "GTK_STOCK_OK:0"
        options["-default"] = "GTK_STOCK_OK"
        return self._call(message, title, options)

    def error(self, message, title):
        self.message(message, title)

    def warning(self, message, title):
        self.message(message, title)

    def _question(self, buttons, message, title):
        options = {}
        options["-buttons"] = buttons
        # options["-default"] = buttons.split(",")[not bool(args["default"])]
        return self._call(message, title, options, useReturnCode=1)

    def ask_ok_cancel(self, message, title):
        return bool(self._question("GTK_STOCK_OK:1,GTK_STOCK_CANCEL:0", message, title))

    def ask_yes_no(self, message, title):
        return bool(self._question("GTK_STOCK_YES:1,GTK_STOCK_NO:0", message, title))

    #    def button_choice(self, args):
    #        buttons = ','.join([ '_%s:%d' % (x, i) for x, i in zip(args['choices'], count()) ])
    #        result = self._question(buttons, args)
    #        return args['choices'][result]

    def ask_string(self, message, title):
        options = {}
        # #        options['-buttons'] = 'GTK_STOCK_OK:1,GTK_STOCK_CANCEL:0'
        # #        options['-default'] = 'GTK_STOCK_OK'
        # if args["default"]:
        #     options["-entrytext"] = args["default"]
        # else:
        options["-entry"] = None
        return self._call(message, title, options)

    def ask_file(self, message, title):
        return self.ask_string(message, title)

    def ask_folder(self, message, title):
        return self.ask_string(message, title)

    def choice(self, choices, message, title):
        return mixins.choice(self, choices, message, title)

    # def multi_choice(self, message, title):
    #     return mixins.multi_choice(self, message, title)
