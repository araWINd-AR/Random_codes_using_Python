import turtle
import math

def draw_radial_burst(color_count, radius, scale):
    screen = turtle.Screen()
    screen.bgcolor("black")
    burst_turtle = turtle.Turtle()
    burst_turtle.speed(0) 
    burst_turtle.pensize(1)
    
   
    colors = ["red", "orange", "yellow", "lime", "cyan", "magenta", "white"]

    
    for angle in range(0, 360 * 3, 3):
        
       
        burst_turtle.pencolor(colors[(angle // 3) % color_count])
        
       
        t = math.radians(angle)
        
        
        r = radius * (1 + scale * math.sin(6 * t)) 
        
        x = r * math.cos(t)
        y = r * math.sin(t)
        
        
        burst_turtle.penup()
        burst_turtle.goto(0, 0)
        burst_turtle.pendown()
        burst_turtle.goto(x, y)

    burst_turtle.hideturtle()
    screen.mainloop()


draw_radial_burst(color_count=7, radius=150, scale=0.5)