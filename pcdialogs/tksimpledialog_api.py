import common_api

##[[[cog
##   import apigen
##   apigen.generateApi('tksimpledialog', 'tkSimpleDialog')
##]]]
def askstring(title, prompt, **kw):
    """Original doc: get a string from the user

    Arguments:

        title -- the dialog title
        prompt -- the label text
        **kw -- see SimpleDialog class

    Return value is a string
    """
    return common_api.askString(title=title, message=prompt)
def askfloat(title, prompt, **kw):
    """Original doc: get a float from the user

    Arguments:

        title -- the dialog title
        prompt -- the label text
        **kw -- see SimpleDialog class

    Return value is a float
    """
    return common_api.askFloat(title=title, message=prompt)
def askinteger(title, prompt, **kw):
    """Original doc: get an integer from the user

    Arguments:

        title -- the dialog title
        prompt -- the label text
        **kw -- see SimpleDialog class

    Return value is an integer
    """
    return common_api.askInteger(title=title, message=prompt)
##[[[end]]] 

