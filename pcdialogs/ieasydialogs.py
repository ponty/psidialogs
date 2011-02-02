"""Easy to use dialogs.

Message(msg) -- display a message and an OK button.
AskString(prompt, default) -- ask for a string, display OK and Cancel buttons.
AskPassword(prompt, default) -- like AskString(), but shows text as bullets.
AskYesNoCancel(question, default) -- display a question and Yes, No and Cancel buttons.
GetArgv(optionlist, commandlist) -- fill a sys.argv-like list using a dialog
AskFileForOpen(...) -- Ask the user for an existing file
AskFileForSave(...) -- Ask the user for an output file
AskFolder(...) -- Ask the user to select a folder
bar = Progress(label, maxvalue) -- Display a progress bar
bar.set(value) -- Set value
bar.inc( *amount ) -- increment value by amount (default=1)
bar.label( *newlabel ) -- get or set text label.

More documentation in each function.
This module uses DLOG resources 260 and on.
Based upon STDWIN dialogs with the same names and functions.
"""


__all__ = ['Message', 'AskString', 'AskPassword', 'AskYesNoCancel',
    'GetArgv', 'AskFileForOpen', 'AskFileForSave', 'AskFolder',
    'ProgressBar']


_dummy_Nav_eventproc = None


def Message(msg, id=260, ok=None):
    """Display a MESSAGE string.

    Return when the user clicks the OK button or presses Return.

    The MESSAGE string can be at most 255 characters long.
    """

def AskString(prompt, default = "", id=261, ok=None, cancel=None):
    """Display a PROMPT string and a text entry field with a DEFAULT string.

    Return the contents of the text entry field when the user clicks the
    OK button or presses Return.
    Return None when the user clicks the Cancel button.

    If omitted, DEFAULT is empty.

    The PROMPT and DEFAULT strings, as well as the return value,
    can be at most 255 characters long.
    """


def AskPassword(prompt,  default='', id=264, ok=None, cancel=None):
    """Display a PROMPT string and a text entry field with a DEFAULT string.
    The string is displayed as bullets only.

    Return the contents of the text entry field when the user clicks the
    OK button or presses Return.
    Return None when the user clicks the Cancel button.

    If omitted, DEFAULT is empty.

    The PROMPT and DEFAULT strings, as well as the return value,
    can be at most 255 characters long.
    """

def AskYesNoCancel(question, default = 0, yes=None, no=None, cancel=None, id=262):
    """Display a QUESTION string which can be answered with Yes or No.

    Return 1 when the user clicks the Yes button.
    Return 0 when the user clicks the No button.
    Return -1 when the user clicks the Cancel button.

    When the user presses Return, the DEFAULT value is returned.
    If omitted, this is 0 (No).

    The QUESTION string can be at most 255 characters.
    """

    def __init__(self, title="Working...", maxval=0, label="", id=263):
        self.w = None
        self.d = None
        _initialize()
        self.d = GetNewDialog(id, -1)
        self.w = self.d.GetDialogWindow()
        self.label(label)
        self.title(title)
        self.set(0, maxval)
        self.d.AutoSizeDialog()
        self.w.ShowWindow()
        self.d.DrawDialog()

    def __del__(self):
        if self.w:
            self.w.BringToFront()
            self.w.HideWindow()
        del self.w
        del self.d

    def title(self, newstr=""):
        """title(text) - Set title of progress window"""
        self.w.BringToFront()
        self.w.SetWTitle(newstr)

    def label(self, *newstr):
        """label(text) - Set text in progress box"""
        self.w.BringToFront()
        if newstr:
            self._label = lf2cr(newstr[0])
        text_h = self.d.GetDialogItemAsControl(2)
        SetDialogItemText(text_h, self._label)

    def _update(self, value):
        maxval = self.maxval
        if maxval == 0:     # an indeterminate bar
            Ctl.IdleControls(self.w)    # spin the barber pole
        else:               # a determinate bar
            if maxval > 32767:
                value = int(value/(maxval/32767.0))
                maxval = 32767
            maxval = int(maxval)
            value = int(value)
            progbar = self.d.GetDialogItemAsControl(3)
            progbar.SetControlMaximum(maxval)
            progbar.SetControlValue(value)  # set the bar length

        # Test for cancel button
        ready, ev = Evt.WaitNextEvent( Events.mDownMask, 1  )
        if ready :
            what,msg,when,where,mod = ev
            part = Win.FindWindow(where)[0]
            if Dlg.IsDialogEvent(ev):
                ds = Dlg.DialogSelect(ev)
                if ds[0] and ds[1] == self.d and ds[-1] == 1:
                    self.w.HideWindow()
                    self.w = None
                    self.d = None
                    raise KeyboardInterrupt, ev
            else:
                if part == 4:   # inDrag
                    self.w.DragWindow(where, screenbounds)
                else:
                    MacOS.HandleEvent(ev)


    def set(self, value, max=None):
        """set(value) - Set progress bar position"""
        if max != None:
            self.maxval = max
            bar = self.d.GetDialogItemAsControl(3)
            if max <= 0:    # indeterminate bar
                bar.SetControlData(0,kControlProgressBarIndeterminateTag,'\x01')
            else:           # determinate bar
                bar.SetControlData(0,kControlProgressBarIndeterminateTag,'\x00')
        if value < 0:
            value = 0
        elif value > self.maxval:
            value = self.maxval
        self.curval = value
        self._update(value)

    def inc(self, n=1):
        """inc(amt) - Increment progress bar position"""
        self.set(self.curval + n)

ARGV_ID=265
ARGV_ITEM_OK=1
ARGV_ITEM_CANCEL=2
ARGV_OPTION_GROUP=3
ARGV_OPTION_EXPLAIN=4
ARGV_OPTION_VALUE=5
ARGV_OPTION_ADD=6
ARGV_COMMAND_GROUP=7
ARGV_COMMAND_EXPLAIN=8
ARGV_COMMAND_ADD=9
ARGV_ADD_OLDFILE=10
ARGV_ADD_NEWFILE=11
ARGV_ADD_FOLDER=12
ARGV_CMDLINE_GROUP=13
ARGV_CMDLINE_DATA=14

def GetArgv(optionlist=None, commandlist=None, addoldfile=1, addnewfile=1, addfolder=1, id=ARGV_ID):
    pass
    
    import aepack
    import Carbon.AE
    import Carbon.File
    for k in args.keys():
        if args[k] is None:
            del args[k]
    # Set some defaults, and modify some arguments
    if not args.has_key('dialogOptionFlags'):
        args['dialogOptionFlags'] = dftflags
    if args.has_key('defaultLocation') and \
            not isinstance(args['defaultLocation'], Carbon.AE.AEDesc):
        defaultLocation = args['defaultLocation']
        if isinstance(defaultLocation, (Carbon.File.FSSpec, Carbon.File.FSRef)):
            args['defaultLocation'] = aepack.pack(defaultLocation)
        else:
            defaultLocation = Carbon.File.FSRef(defaultLocation)
            args['defaultLocation'] = aepack.pack(defaultLocation)
    if args.has_key('typeList') and not isinstance(args['typeList'], Carbon.Res.ResourceType):
        typeList = args['typeList'][:]
        # Workaround for OSX typeless files:
        if 'TEXT' in typeList and not '\0\0\0\0' in typeList:
            typeList = typeList + ('\0\0\0\0',)
        data = 'Pyth' + struct.pack("hh", 0, len(typeList))
        for type in typeList:
            data = data+type
        args['typeList'] = Carbon.Res.Handle(data)
    tpwanted = str
    if args.has_key('wanted'):
        tpwanted = args['wanted']
        del args['wanted']
    return args, tpwanted

def AskFileForOpen(
        message=None,
        typeList=None,
        # From here on the order is not documented
        version=None,
        defaultLocation=None,
        dialogOptionFlags=None,
        location=None,
        clientName=None,
        windowTitle=None,
        actionButtonLabel=None,
        cancelButtonLabel=None,
        preferenceKey=None,
        popupExtension=None,
        eventProc=_dummy_Nav_eventproc,
        previewProc=None,
        filterProc=None,
        wanted=None,
        multiple=None):
    """Display a dialog asking the user for a file to open.

    wanted is the return type wanted: FSSpec, FSRef, unicode or string (default)
    the other arguments can be looked up in Apple's Navigation Services documentation"""


def AskFileForSave(
        message=None,
        savedFileName=None,
        # From here on the order is not documented
        version=None,
        defaultLocation=None,
        dialogOptionFlags=None,
        location=None,
        clientName=None,
        windowTitle=None,
        actionButtonLabel=None,
        cancelButtonLabel=None,
        preferenceKey=None,
        popupExtension=None,
        eventProc=_dummy_Nav_eventproc,
        fileType=None,
        fileCreator=None,
        wanted=None,
        multiple=None):
    """Display a dialog asking the user for a filename to save to.

    wanted is the return type wanted: FSSpec, FSRef, unicode or string (default)
    the other arguments can be looked up in Apple's Navigation Services documentation"""



def AskFolder(
        message=None,
        # From here on the order is not documented
        version=None,
        defaultLocation=None,
        dialogOptionFlags=None,
        location=None,
        clientName=None,
        windowTitle=None,
        actionButtonLabel=None,
        cancelButtonLabel=None,
        preferenceKey=None,
        popupExtension=None,
        eventProc=_dummy_Nav_eventproc,
        filterProc=None,
        wanted=None,
        multiple=None):
    """Display a dialog asking the user for select a folder.

    wanted is the return type wanted: FSSpec, FSRef, unicode or string (default)
    the other arguments can be looked up in Apple's Navigation Services documentation"""



