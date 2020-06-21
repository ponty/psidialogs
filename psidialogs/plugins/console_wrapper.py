from psidialogs.unicodeutil import ansi_dialog_eg as ansi_dialog
from psidialogs.iplugin import IPlugin
from psidialogs.util import py2


def text_input(msg):
    if py2():
        return raw_input(msg)
    else:
        return input(msg)


class Backend(IPlugin):
    console = True
    backend = "console"
    name = "console"

    @ansi_dialog
    def message(self, args):
        msg = args["message"] + "[ENTER]"
        text_input(msg)

    @ansi_dialog
    def ask_string(self, args):
        answer = text_input(args["message"])
        return answer

    @ansi_dialog
    def ask_yes_no(self, args):
        msg = args["message"]
        msg += " [Yes/No] "
        answers_yes = "yes y".split()
        answers_no = "no n".split()
        answers = answers_yes + answers_no
        s = ""
        while 1:
            s = text_input(msg)
            s = s.lower().strip()
            if s in answers:
                break

        b = s in answers_yes

        return b

    def ask_ok_cancel(self, args):
        return self.ask_yes_no(args)

    def warning(self, args):
        args["message"] = "[WARNING] " + args["message"]
        return self.message(args)

    def error(self, args):
        args["message"] = "[ERROR] " + args["message"]
        return self.message(args)
