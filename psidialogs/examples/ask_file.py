import psidialogs

f = psidialogs.ask_file("Select a file!")
if f is not None:
    print(f)
