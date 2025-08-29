"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk
root = Tk()
root.withdraw()

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    name = simpledialog.askstring(title="user", prompt="Wat iz ur name?")
    for i in range(len(name)):
       # print( name[i]  )
        if i % 2 == 0:
            print(name[i].upper(), end="")
        if i % 2 == 1:
            print(name[i], end="")
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton,
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    pass
