import psidialogs

def textbox(message='', title='', text='', codebox=0):
    """Original doc: Display some text in a proportional font with line wrapping at word breaks.
	This function is suitable for displaying general written text.

	The text parameter should be a string, or a list or tuple of lines to be
	displayed in the textbox.
	"""
    return psidialogs.text(message=message, title=title, text=text)

def buttonbox(message='Shall I continue?', title='', choices=['Button1', 'Button2', 'Button3']):
    """Original doc: Display a message, a title, and a set of buttons.
	The buttons are defined by the members of the choices list.
	Return the text of the button that the user selected.
	"""
    raise NotImplementedError()
#    return psidialogs.button_choice(message=message, title=title, choices=choices)

def filesavebox(msg=None, title=None, argInitialFile=None):
    """Original doc: A file to get the name of a file to save.
	Returns the name of a file, or None if user chose to cancel.

	if argInitialFile contains a valid filename, the dialog will
	be positioned at that file when it appears.
	"""
    return psidialogs.ask_file(message=msg, title=title, default=argInitialFile, save=True)

def diropenbox(msg=None, title=None, argInitialDir=None):
    """Original doc: A dialog to get a directory name.
	Note that the msg argument, if specified, is ignored.

	Returns the name of a directory, or None if user chose to cancel.

	If an initial directory is specified in argument 3,
	and that directory exists, then the
	dialog box will start with that directory.
	"""
    return psidialogs.ask_folder(message=msg, title=title, default=argInitialDir)

def ynbox(message='Shall I continue?', title=''):
    """Original doc: Display a message box with choices of Yes and No.
	The default is "Yes".
	Returns returns 1 if "Yes" is chosen, or if
	the dialog is cancelled (which is interpreted as
	choosing the default).  Otherwise returns 0.

	If invoked without a message parameter, displays a generic request for a confirmation
	that the user wishes to continue.  So it can be used this way:

		if ynbox(): pass # continue
		else: sys.exit(0)  # exit the program
	"""
    return psidialogs.ask_yes_no(message=message, title=title)

def choicebox(message='Pick something.', title='', choices=['program logic error - no choices specified']):
    """Original doc: Present the user with a list of choices.
	return the choice that he selects.
	return None if he cancels the selection selection.
	"""
    return psidialogs.choice(message=message, title=title, choices=choices)

def msgbox(message='Shall I continue?', title='', buttonMessage='OK'):
    """Original doc: Display a messagebox
	"""
    return psidialogs.message(message=message, title=title, ok=buttonMessage)

def multchoicebox(message='Pick as many items as you like.', title='', choices=['program logic error - no choices specified']):
    """Original doc: Present the user with a list of choices.
	allow him to select multiple items and return them in a list.
	if the user doesn't choose anything from the list, return the empty list.
	return None if he cancelled selection.
	"""
    return psidialogs.multi_choice(message=message, title=title, choices=choices)

def enterbox(message='Enter something.', title='', argDefaultText=''):
    """Original doc: Show a box in which a user can enter some text.
	You may optionally specify some default text, which will appear in the
	enterbox when it is displayed.
	Returns the text that the user entered, or None if he cancels the operation.
	"""
    return psidialogs.ask_string(message=message, title=title, default=argDefaultText)

def passwordbox(message='Enter your password.', title='', argDefaultPassword=''):
    """Original doc: Show a box in which a user can enter a password.
	The text is masked with asterisks, so the password is not displayed.
	Returns the text that the user entered, or None if he cancels the operation.
		"""
    raise NotImplementedError()

def fileopenbox(msg=None, title=None, argInitialFile=None):
    """Original doc: A dialog to get a file name.
	Returns the name of a file, or None if user chose to cancel.

	if argInitialFile contains a valid filename, the dialog will
	be positioned at that file when it appears.
	"""
    return psidialogs.ask_file(message=msg, title=title, default=argInitialFile)

def integerbox(message='Enter something.', title='', argDefault=None, argLowerBound=0, argUpperBound=99):
    """Original doc: Show a box in which a user can enter an integer.
	In addition to arguments for message and title, this function accepts
	integer arguments for default_value, lowerbound, and upperbound.

	The default_value argument may be None.

	When the user enters some text, the text is checked to verify
	that it can be converted to an integer between the lowerbound and upperbound.

	If it can be, the integer (not the text) is returned.

	If it cannot, then an error message is displayed, and the integerbox is
		redisplayed.

	If the user cancels the operation, the default value is returned.
	"""
    return psidialogs.ask_string(message=message, title=title, default=str(argDefault))
##[[[end]]] 

# copy from easygui.py
def codebox(message="", title="", text=""):
    """
    Original doc:
    Display some text in a monospaced font, with no line wrapping.
    This function is suitable for displaying code and text that is
    formatted using spaces.

    The text parameter should be a string, or a list or tuple of lines to be
    displayed in the textbox.
    """
    textbox(message, title, text, codebox=1 )

# copy from easygui.py
def ccbox(message="Shall I continue?", title=""):
    """
    Original doc:
    Display a message box with choices of Continue and Cancel.
    The default is "Continue".
    Returns returns 1 if "Continue" is chosen, or if
    the dialog is cancelled (which is interpreted as
    choosing the default).  Otherwise returns 0.

    If invoked without a message parameter, displays a generic request for a confirmation
    that the user wishes to continue.  So it can be used this way:

        if ccbox(): pass # continue
        else: sys.exit(0)  # exit the program
    """
    choices = ["Continue", "Cancel"]
    if title == None: title = ""
    return boolbox(message, title, choices)

# copy from easygui.py
def boolbox(message="Shall I continue?", title="", choices=["Yes","No"]):
    """
    Original doc:
    Display a boolean message box.
    The default is the first choice.
    Returns returns 1 if the first choice is chosen, or if
    the dialog is cancelled (which is interpreted as
    choosing the default).  Otherwise returns 0.
    """
    if title == None:
        if message == "Shall I continue?": title = "Confirmation"
        else: title = ""


    reply = buttonbox(message, title, choices)
    if reply == choices[0]: return 1
    else: return 0

# copy from easygui.py
def indexbox(message="Shall I continue?", title="", choices=["Yes","No"]):
    """
    Original doc:
    Display a buttonbox with the specified choices.
    Return the index of the choice selected.
    """
    reply = buttonbox(message, title, choices)
    index = -1
    for choice in choices:
        index = index + 1
        if reply == choice: return index
