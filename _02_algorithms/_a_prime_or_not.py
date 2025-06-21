"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk
root = Tk()
root.withdraw()

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number.
    number = simpledialog.askinteger(title="b", prompt="Type a number between 2 and a trillion.")
    for i in range(2, number):
        if number % i == 0:
            messagebox.showinfo(title="d", message=f"{number} is not prime because it is divisible by {i}.")
            quit()
    messagebox.showinfo(title="d", message=f"{number} is prime.")

    #  2. Use a for loop, if statement, and mod
    #         print(i)ulo to find if the number
    #     is prime.

    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
