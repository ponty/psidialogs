from psidialogs import backend_api
import logging

__version__='0.0.6'
log = logging.getLogger(__name__)
log.debug('version=' + __version__)

def message(message, title=''):
    """
    Display a message
    
    :ref:`screenshots<message>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None
    """
    return backend_api.opendialog("message" , dict(message=message, title=title))

def error(message='Error!', title=''):
    """
    Display a warning message

    :ref:`screenshots<error>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None
    """
    return backend_api.opendialog("error" , dict(message=message, title=title))

def warning(message='Warning!', title=''):
    """
    Display an error message

    :ref:`screenshots<warning>`

    :param message: message to be displayed.
    :param title: window title
    :rtype: None
    """
    return backend_api.opendialog("warning" , dict(message=message, title=title))

def text(text, message='', title=''):
    """
    This function is suitable for displaying general text, which can be longer
    than in :func:`message` 
    
    :ref:`screenshots<text>`

    :param text: (long) text to be displayed 
    :param message: (short) message to be displayed.
    :param title: window title
    :rtype: None
    """
    return backend_api.opendialog("text" , dict(text=text, message=message, title=title))


def ask_string(message='Enter something.', default='', title=''):
    """
    Show a box in which a user can enter some text.

    You may optionally specify some default text, which will appear in the
    entry-box when it is displayed.

    Returns the text that the user entered, or None if he cancels the operation
    
    :ref:`screenshots<ask_string>`

    :param message: message to be displayed.
    :param title: window title
    :param default: entry-box default string
    :param ok: label of the ok button
    :param cancel: label of the cancel button
    :rtype: None or string
    """
    return backend_api.opendialog("ask_string" , dict(message=message, default=default, title=title))

def ask_file(message='Select file for open.', default='', title='', save=False):
    """
    A dialog to get a file name.
    The "default" argument specifies a file path.
    
    save=False -> file for loading
    save=True -> file for saving
    
    Return the file path that the user entered, or None if he cancels the operation.

    :param message: message to be displayed.
    :param save: bool 0 -> load , 1 -> save
    :param title: window title
    :param default: default file path
    :rtype: None or string
    """
    return backend_api.opendialog("ask_file" , dict(message=message, default=default, title=title, save=save))

def ask_folder(message='Select folder.', default='', title=''):
    """
    A dialog to get a directory name.
    Returns the name of a directory, or None if user chose to cancel.
    If the "default" argument specifies a directory name, and that
    directory exists, then the dialog box will start with that directory.

    :param message: message to be displayed.
    :param title: window title
    :param default: default folder path
    :param ok: label of the ok button
    :param cancel: label of the cancel button
    :rtype: None or string
    """
    return backend_api.opendialog("ask_folder" , dict(message=message, default=default, title=title))

def choice(choices=[], message='Pick something.', default=None, title=''):
    """
    Present the user with a list of choices.
    return the choice that he selects.
    return None if he cancels the selection selection.

    :ref:`screenshots<choice>`

    :param choices: a list of the choices to be displayed
    :param message: message to be displayed.
    :param title: window title
    :param default: default string of choice
    :rtype: None or string
    """
    return backend_api.opendialog("choice" , dict(choices=choices, message=message, default=default, title=title))

def multi_choice(choices=[], message='Pick as many items as you like.', default=None, title=''):
    """
    Present the user with a list of choices.
    allow him to select multiple items and return them in a list.
    if the user doesn't choose anything from the list, return the empty list.
    return None if he cancelled selection.

    :ref:`screenshots<multi_choice>`

    :param choices: a list of the choices to be displayed
    :param message: message to be displayed.
    :param title: window title
    :param default: default list of strings
    :rtype: None or list of strings
    """
    return backend_api.opendialog("multi_choice" , dict(choices=choices, message=message, default=default, title=title))

def ask_ok_cancel(message='', default=0, title=''):
    """
    Display a message with choices of OK and Cancel.

    returned value:
        OK       -> True
        Cancel   -> False

    :ref:`screenshots<ask_ok_cancel>`
    
    :param message: message to be displayed.
    :param title: window title
    :param default: default button as boolean (OK=True, Cancel=False)
    :rtype: bool
    """
    return backend_api.opendialog("ask_ok_cancel" , dict(message=message, default=default, title=title))

def ask_yes_no(message='', default=0, title=''):
    """
    Display a message with choices of Yes and No.

    returned value:
        Yes  -> True
        No   -> False
    
    :ref:`screenshots<ask_yes_no>`

    :param message: message to be displayed.
    :param title: window title
    :param default: default button as boolean (YES=True, NO=False)
    :rtype: bool
    """
    return backend_api.opendialog("ask_yes_no" , dict(message=message, default=default, title=title))

FUNCTIONS=[
           message,
           ask_string,
           ask_file, 
           ask_folder,
           choice,
           multi_choice, 
           text, 
           error,
           warning,
           ask_ok_cancel,
           ask_yes_no,
#           button_choice,           
           ]

FUNCTION_NAMES=sorted(map(lambda x :x.__name__,FUNCTIONS))
