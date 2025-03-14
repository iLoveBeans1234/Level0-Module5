"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def draw_square(t):
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)

def draw_circle(t):
    turtle.circle(150)

def draw_triangle(t):
    for i in range(3):
        turtle.forward(150)
        turtle.left(120)


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    bob = turtle.Turtle()
    bob.shape('turtle')
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    while True:
        #   3. Ask the user for the for a shape to draw.
        user = simpledialog.askstring(title="user", prompt="What shape do you want to draw?")
        if user == "square":
            draw_square(bob)
        elif user == "circle":
            draw_circle(bob)
        elif user == "triangle":
            draw_triangle(bob)
        else:
            exit()
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass



