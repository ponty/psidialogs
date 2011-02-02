import common_api

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


##[[[cog
##   import apigen
##   apigen.generateApi('tkfiledialog', 'tkFileDialog')
##]]]
def askopenfilenames(**options):
    """Original doc: Ask for multiple filenames to open

    Returns a list of filenames or empty list if
    cancel button selected
    """
    return common_api.askFilesForOpen()
def askopenfilename(**options):
    """Original doc: Ask for a filename to open"""
    return common_api.askFileForOpen()
def askdirectory(**options):
    """Original doc: Ask for a directory, and return the file name"""
    return common_api.askFolder()
def asksaveasfilename(**options):
    """Original doc: Ask for a filename to save as"""
    return common_api.askFileForSave()
##[[[end]]] 

