"""
Go to the recipe to run the demonstration before starting this program
"""
global x_position
def setup():
    global x_position
    x_position = 500
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(1800, 500)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
def draw():
    global x_position
    background(255,255,255)
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    for i in range(10, 500, 40):
        ellipse(x_position, 250, i, i)
    for i in range(10, 500, 40):
        ellipse(1300, 250, i, i)
    x_position += 1

    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
    
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */

         
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
