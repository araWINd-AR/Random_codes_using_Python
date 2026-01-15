import turtle

def draw_enhanced_rosette(sides, repetitions, size):
    """
    Draws a complex, multi-colored rosette pattern.
    """
    screen = turtle.Screen()
    screen.bgcolor("black") # Use a black background for maximum contrast
    rosette_turtle = turtle.Turtle()
    rosette_turtle.pensize(2)
    rosette_turtle.speed(0) # Fastest drawing speed

    # Define a list of vibrant colors
    colors = ['cyan', 'magenta', 'yellow', 'lime', 'red', 'blue']

    # Calculate the angles
    turn_angle = 360 / sides           
    repetition_angle = 360 / repetitions 
    
    # Main loop to repeat the polygon
    for i in range(repetitions):
        # Change color for each new polygon
        rosette_turtle.pencolor(colors[i % len(colors)])
        
        # Inner loop to draw the polygon 
        for _ in range(sides):
            rosette_turtle.forward(size)
            rosette_turtle.right(turn_angle)
        
        # Rotate the entire turtle slightly before drawing the next polygon
      
        rosette_turtle.right(repetition_angle + 1) 

    rosette_turtle.hideturtle()
    screen.mainloop()

# --- Call the function for a complex, colorful design ---
draw_enhanced_rosette(sides=8, repetitions=60, size=40)
