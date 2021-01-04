import psidialogs

psidialogs.set_backend_preference(["tkinter", "zenity"])
print(psidialogs.backends())
psidialogs.message("Hello!")
