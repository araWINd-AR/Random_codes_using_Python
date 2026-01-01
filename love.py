import turtle
import math

def draw_math_heart(scale):
    """
    Draws a heart shape using a mathematical formula 
    (polar coordinates converted to cartesian coordinates).

    Args:
        scale (float): Controls the overall size of the heart.
    """
    # 1. Setup
    screen = turtle.Screen()
    heart_turtle = turtle.Turtle()
    heart_turtle.pencolor('red')
    heart_turtle.fillcolor('red')
    heart_turtle.pensize(2)
    heart_turtle.speed(0) # Fastest drawing speed

    # 2. Positioning: Start the drawing off-center so the heart is centered
    heart_turtle.penup()
    heart_turtle.goto(0, -scale * 2.5) # Move down slightly to center the V-tip
    heart_turtle.pendown()

    # 3. Draw and Fill the Heart using the formula
    heart_turtle.begin_fill()
    
    # Loop through angles (t) from 0 to 6.28 (approx 2*pi radians)
    # The step (0.1) controls the smoothness and speed
    for t in range(0, 628):
        t = t / 100.0 # Convert the integer loop to floating point radians

        # Heart Formula (Parametric Equations):
        # x = scale * 16 * sin(t)^3
        # y = scale * (13*cos(t) - 5*cos(2t) - 2*cos(3t) - cos(4t))
        
        x = scale * 16 * math.sin(t)**3
        y = scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

        heart_turtle.goto(x, y) # Move the turtle to the calculated point

    heart_turtle.end_fill()

    # 4. Finish
    heart_turtle.hideturtle()
    screen.mainloop()

# --- Call the function to draw your heart ---
# Use a scale factor of 10 for a visible, centered heart
draw_math_heart(scale=10)