import psidialogs

name = psidialogs.ask_string("What is your name?")
if name is not None:
    print(name)
