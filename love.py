import turtle
import math

def draw_math_heart(scale):
    
#  Setup
    screen = turtle.Screen()
    heart_turtle = turtle.Turtle()
    heart_turtle.pencolor('red')
    heart_turtle.fillcolor('red')
    heart_turtle.pensize(2)
    heart_turtle.speed(0)                
    heart_turtle.penup()
    heart_turtle.goto(0, -scale * 2.5) 
    heart_turtle.pendown()
    heart_turtle.begin_fill()
    for t in range(0, 628):
        t = t / 100.0 
        x = scale * 16 * math.sin(t)**3
        y = scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

        heart_turtle.goto(x, y) 
    heart_turtle.end_fill()

  
    heart_turtle.hideturtle()
    screen.mainloop()

draw_math_heart(scale=10)

