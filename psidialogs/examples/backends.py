import psidialogs

print(psidialogs.backends())
psidialogs.set_backend_preference(["tkinter", "zenity"])
print(psidialogs.backends())
