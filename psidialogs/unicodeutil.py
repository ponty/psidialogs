def uniencode(s):
    if isinstance(s, str):
        s = s.encode("utf-8")
    return s


def unidecode(s):
    if isinstance(s, bytes):
        s = s.decode("utf-8", "ignore")
    return s
