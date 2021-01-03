from psidialogs.iplugin import IPlugin


class ConsoleWrapper(IPlugin):
    console = True
    name = "console"

    def message(self, message, title):
        msg = message + "[ENTER]"
        input(msg)

    def ask_string(self, message, title):
        answer = input(message)
        return answer

    def ask_yes_no(self, message, title):
        msg = message
        msg += " [Yes/No] "
        answers_yes = "yes y".split()
        answers_no = "no n".split()
        answers = answers_yes + answers_no
        s = ""
        while 1:
            s = input(msg)
            s = s.lower().strip()
            if s in answers:
                break

        b = s in answers_yes

        return b

    def ask_ok_cancel(self, message, title):
        return self.ask_yes_no(message, title)

    def warning(self, message, title):
        message = "[WARNING] " + message
        return self.message(message, title)

    def error(self, message, title):
        message = "[ERROR] " + message
        return self.message(message, title)
