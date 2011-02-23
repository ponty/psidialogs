import psidialogs

def AskFileForSave(message=None, savedFileName=None, version=None, defaultLocation=None, dialogOptionFlags=None, location=None, clientName=None, windowTitle=None, actionButtonLabel=None, cancelButtonLabel=None, preferenceKey=None, popupExtension=None, eventProc=None, fileType=None, fileCreator=None, wanted=None, multiple=None):
    """Original doc: Display a dialog asking the user for a filename to save to.

    wanted is the return type wanted: FSSpec, FSRef, unicode or string (default)
    the other arguments can be looked up in Apple's Navigation Services documentation"""
    return psidialogs.ask_file(message=message, save=True)
def AskFileForOpen(message=None, typeList=None, version=None, defaultLocation=None, dialogOptionFlags=None, location=None, clientName=None, windowTitle=None, actionButtonLabel=None, cancelButtonLabel=None, preferenceKey=None, popupExtension=None, eventProc=None, previewProc=None, filterProc=None, wanted=None, multiple=None):
    """Original doc: Display a dialog asking the user for a file to open.

    wanted is the return type wanted: FSSpec, FSRef, unicode or string (default)
    the other arguments can be looked up in Apple's Navigation Services documentation"""
    return psidialogs.ask_file(message=message)
def AskPassword(prompt, default='', id=264, ok=None, cancel=None):
    """Original doc: Display a PROMPT string and a text entry field with a DEFAULT string.
    The string is displayed as bullets only.

    Return the contents of the text entry field when the user clicks the
    OK button or presses Return.
    Return None when the user clicks the Cancel button.

    If omitted, DEFAULT is empty.

    The PROMPT and DEFAULT strings, as well as the return value,
    can be at most 255 characters long.
    """
    raise NotImplementedError()

def ask_folder(message=None, version=None, defaultLocation=None, dialogOptionFlags=None, location=None, clientName=None, windowTitle=None, actionButtonLabel=None, cancelButtonLabel=None, preferenceKey=None, popupExtension=None, eventProc=None, filterProc=None, wanted=None, multiple=None):
    """Original doc: Display a dialog asking the user for select a folder.

    wanted is the return type wanted: FSSpec, FSRef, unicode or string (default)
    the other arguments can be looked up in Apple's Navigation Services documentation"""
    return psidialogs.ask_folder(message=message, title=windowTitle, ok=actionButtonLabel, cancel=cancelButtonLabel)
def AskString(prompt, default='', id=261, ok=None, cancel=None):
    """Original doc: Display a PROMPT string and a text entry field with a DEFAULT string.

    Return the contents of the text entry field when the user clicks the
    OK button or presses Return.
    Return None when the user clicks the Cancel button.

    If omitted, DEFAULT is empty.

    The PROMPT and DEFAULT strings, as well as the return value,
    can be at most 255 characters long.
    """
    return psidialogs.ask_string(message=prompt, default=default, ok=ok, cancel=cancel)
def Message(msg, id=260, ok=None):
    """Original doc: Display a MESSAGE string.

    Return when the user clicks the OK button or presses Return.

    The MESSAGE string can be at most 255 characters long.
    """
    return psidialogs.message(message=msg, ok=ok)

