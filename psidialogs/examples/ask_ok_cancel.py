import psidialogs

ok = psidialogs.ask_ok_cancel("Do you want to continue?")
if ok:
    print("continue")
