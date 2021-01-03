import logging

from psidialogs.about import __version__
from psidialogs.childproc import childprocess_backend_version
from psidialogs.loader import _opendialog, backend_dict

log = logging.getLogger(__name__)
log.debug("version=%s", __version__)


def message(message, title="", backend=None):
    """
    Display a message

    :ref:`screenshots<message>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None
    """
    return dialog("message", message=message, title=title, backend=backend)


def error(message="Error!", title="", backend=None):
    """
    Display an error message

    :ref:`screenshots<error>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None
    """
    return dialog("error", message=message, title=title, backend=backend)


def warning(message="Warning!", title="", backend=None):
    """
    Display a warning message

    :ref:`screenshots<warning>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None
    """
    return dialog("warning", message=message, title=title, backend=backend)


# def text(text, message="", title=""):
#     """
#     This function is suitable for displaying general text, which can be longer
#     than in :func:`message`

#     :ref:`screenshots<text>`

#     :param text: (long) text to be displayed
#     :param message: (short) message to be displayed.
#     :param title: window title
#     :rtype: None
#     """
#     return opendialog("text", dict(text=text, message=message, title=title))


def ask_string(message="Enter something.", title="", backend=None):
    """
    Show a box in which a user can enter some text.

    Returns the text that the user entered, or None if he cancels the operation

    :ref:`screenshots<ask_string>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None or string
    """
    return dialog("ask_string", message=message, title=title, backend=backend)


def ask_file(message="Select file for open.", title="", backend=None):
    """
    A dialog to get a file name.

    Return the file path that the user entered, or None if he cancels the operation.

    :param message: message to be displayed.
    :param title: window title
    :rtype: None or string
    """
    return dialog("ask_file", message=message, title=title, backend=backend,)


def ask_folder(message="Select folder.", title="", backend=None):
    """
    A dialog to get a directory name.
    Returns the name of a directory, or None if user chose to cancel.

    :param message: message to be displayed.
    :param title: window title
    :rtype: None or string
    """
    return dialog("ask_folder", message=message, title=title, backend=backend)


def choice(choices=[], message="Pick something.", title="", backend=None):
    """
    Present the user with a list of choices.
    return the choice that he selects.
    return None if he cancels the selection selection.

    :ref:`screenshots<choice>`

    :param choices: a list of the choices to be displayed
    :param message: message to be displayed.
    :param title: window title
    :rtype: None or string
    """
    return dialog(
        "choice", choices=choices, message=message, title=title, backend=backend,
    )


# def multi_choice(
#     choices=[], message="Pick as many items as you like.", title="", backend=None,
# ):
#     """
#     Present the user with a list of choices.
#     allow him to select multiple items and return them in a list.
#     if the user doesn't choose anything from the list, return the empty list.
#     return None if he cancelled selection.

#     :ref:`screenshots<multi_choice>`

#     :param choices: a list of the choices to be displayed
#     :param message: message to be displayed.
#     :param title: window title
#     :rtype: None or list of strings
#     """
#     if len(choices) == 0:
#         log.warning("choices=[] returning None")
#         return None
#     return opendialog(
#         "multi_choice", dict(choices=choices, message=message, title=title), backend,
#     )


def ask_ok_cancel(message="", title="", backend=None):
    """
    Display a message with choices of OK and Cancel.

    returned value:
        OK       -> True
        Cancel   -> False

    :ref:`screenshots<ask_ok_cancel>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: bool
    """
    return dialog("ask_ok_cancel", message=message, title=title, backend=backend)


def ask_yes_no(message="", title="", backend=None):
    """
    Display a message with choices of Yes and No.

    returned value:
        Yes  -> True
        No   -> False

    :ref:`screenshots<ask_yes_no>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: bool
    """
    return dialog("ask_yes_no", message=message, title=title, backend=backend)


FUNCTIONS = [
    message,
    warning,
    error,
    ask_ok_cancel,
    ask_yes_no,
    ask_string,
    ask_file,
    ask_folder,
    choice,
    # multi_choice,
]

FUNCTION_NAMES = list(map(lambda x: x.__name__, FUNCTIONS))


def backends():
    """Back-end names as a list.

    :return: back-ends as string list
    """
    return list(backend_dict.keys())


def backend_version(backend):
    """Back-end version.

    :param backend: back-end (examples:pyqt5, tkinter,..)
    :return: version as string
    """
    return childprocess_backend_version(backend)


def dialog(funcname, choices=[], message="", title="", backend=None, childprocess=True):
    if funcname == "choice":
        if len(choices) == 0:
            log.warning("choices=[] returning None")
            return None
        if len(choices) == 1:
            log.warning("choices has one element only")
            return choices[0]
    if not title:
        title = "psidialogs"
    return _opendialog(
        funcname,
        dict(choices=choices, message=message, title=title),
        backend,
        childprocess=childprocess,
    )
