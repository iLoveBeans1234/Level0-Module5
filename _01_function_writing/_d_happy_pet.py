"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk
root = Tk()
root.withdraw()

global happiness_level
happiness_level = 50

def walkPet(pet):
    global happiness_level
    if pet in ["dog", "cat", "guinea pig", "horse", "donkey"]:
        messagebox.showinfo(title="user", message=f"Your {pet} is happy.")
        happiness_level += 20
    if pet == "fish":
        messagebox.showinfo(title="user", message=f"Your {pet} is not happy.")
        happiness_level -= 20
def feedPet(pet):
    global happiness_level
    messagebox.showinfo(title="user", message=f"Your {pet} is happy.")
    happiness_level += 20
def killPet(pet):
    global happiness_level
    messagebox.showinfo(title="user", message="Thank you for killing your pet. It looked very ugly.")
if __name__== '__main__' :
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    pet = simpledialog.askstring(title="user", prompt="What pet do u want? Dog, cat, fish, guinea pig, horse, or donkey?")

    while True:
        activity = simpledialog.askstring(title="user", prompt=f"What activity would u like ur pet to do? Happiness = {happiness_level}/100")
        if activity == None or activity == '':
            exit()
        if activity == "walk":
            walkPet(pet)

        if activity == "feed":
            feedPet(pet)

        if activity == "kill":
            killPet(pet)


    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
        if happiness_level >= 100:
            messagebox.showinfo(title="user", message=f"Ur {pet} is at da max happinezzzzzzz.")
            exit()
        if happiness_level <= 0:
            messagebox.showinfo(title="user", message=f"Ur {pet} is so stupid because it are not happy.")
