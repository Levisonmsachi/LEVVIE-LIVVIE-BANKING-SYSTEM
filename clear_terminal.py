import os

def clear():
    # Windows
    if os.name == 'nt':
        os.system('cls')

    # Mac & Linux (posix systems)
    else:
        os.system('clear')
