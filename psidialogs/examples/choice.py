import psidialogs

s = psidialogs.choice(["1", "2", "3"], "Choose a number!")
if s is not None:
    print(s)
