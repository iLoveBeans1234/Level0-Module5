"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    simpledialog.askstring(title="user", prompt="What pet do you want? Dog, cat, fish, guinea pig, horse, donkey?")
    while True:
        simpledialog.askstring(title="user")
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
