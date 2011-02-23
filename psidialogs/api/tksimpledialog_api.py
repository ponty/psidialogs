from psidialogs.api.ask_number import ask_float, ask_int
import psidialogs

def askstring(title, prompt, **kw):
    """Original doc: get a string from the user

    Arguments:

        title -- the dialog title
        prompt -- the label text
        **kw -- see SimpleDialog class

    Return value is a string
    """
    return psidialogs.ask_string(title=title, message=prompt)

def askfloat(title, prompt, **kw):
    """Original doc: get a float from the user

    Arguments:

        title -- the dialog title
        prompt -- the label text
        **kw -- see SimpleDialog class

    Return value is a float
    """
    return ask_float(title=title, message=prompt)

def askinteger(title, prompt, **kw):
    """Original doc: get an integer from the user

    Arguments:

        title -- the dialog title
        prompt -- the label text
        **kw -- see SimpleDialog class

    Return value is an integer
    """
    return ask_int(title=title, message=prompt)


