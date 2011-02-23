import psidialogs

def askopenfile(mode = "r", **options):
    "Ask for a filename to open, and returned the opened file"

    filename = askopenfilename(**options)
    if filename:
        return open(filename, mode)
    return None

def askopenfiles(mode = "r", **options):
    """Ask for multiple filenames and return the open file
    objects

    returns a list of open file objects or an empty list if
    cancel selected
    """

    files = askopenfilenames(**options)
    if files:
        ofiles=[]
        for filename in files:
            ofiles.append(open(filename, mode))
        files=ofiles
    return files


def asksaveasfile(mode = "w", **options):
    "Ask for a filename to save as, and returned the opened file"

    filename = asksaveasfilename(**options)
    if filename:
        return open(filename, mode)
    return None

def askopenfilenames(**options):
    """Original doc: Ask for multiple filenames to open

    Returns a list of filenames or empty list if
    cancel button selected
    """
    raise NotImplementedError()

def askopenfilename(**options):
    """Original doc: Ask for a filename to open"""
    return psidialogs.ask_file(save=False)

def askdirectory(**options):
    """Original doc: Ask for a directory, and return the file name"""
    return psidialogs.ask_folder()

def asksaveasfilename(**options):
    """Original doc: Ask for a filename to save as"""
    return psidialogs.ask_file(save=True)

