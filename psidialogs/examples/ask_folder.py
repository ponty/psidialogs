import psidialogs

f = psidialogs.ask_folder("Select a folder!")
if f is not None:
    print(f)
