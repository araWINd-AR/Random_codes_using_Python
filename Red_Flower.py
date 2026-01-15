import turtle

def draw_rosette(sides, repetitions, size, color):
    """
    Draws a flower-like rosette shape by repeating a polygon.

    Args:
        sides (int): Number of sides for the inner polygon (e.g., 6 for a hexagon).
        repetitions (int): How many times to repeat the polygon (e.g., 36).
        size (int): Length of each side of the inner polygon.
        color (str): The color to draw the rosette with.
    """
    screen = turtle.Screen()
    screen.bgcolor("white") 
    rosette_turtle = turtle.Turtle()
    rosette_turtle.color(color)
    rosette_turtle.pensize(1)
    rosette_turtle.speed(0) 

    # Calculate the angles
    turn_angle = 360 / sides           # Angle to turn for one side of the polygon
    repetition_angle = 360 / repetitions # Small angle to rotate between polygons
    
    # Main loop to repeat the polygon
    for _ in range(repetitions):
        # Inner loop to draw the polygon (e.g., a hexagon or a square)
        for _ in range(sides):
            rosette_turtle.forward(size)
            rosette_turtle.right(turn_angle)
        
        # Rotate the entire turtle slightly before drawing the next polygon
        rosette_turtle.right(repetition_angle)

    rosette_turtle.hideturtle()
    screen.mainloop()

# --- Call the function ---
# Example: Draws a shape made of 36 hexagons, each side 50 units long, in red
draw_rosette(sides=6, repetitions=36, size=50, color='red')