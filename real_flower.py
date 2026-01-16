import turtle
import math

def draw_real_flower(petal_color='red', center_color='yellow', stem_color='green'):
    
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("lightblue")
    flower_turtle = turtle.Turtle()
    flower_turtle.speed(0)
    flower_turtle.hideturtle() 
    petal_size = 50
    center_radius = 20
    petal_center_y = 50 
    flower_turtle.penup()
    flower_turtle.goto(0, -250)
    flower_turtle.setheading(90) 
    flower_turtle.pendown()
    flower_turtle.color(stem_color)
    flower_turtle.pensize(5)
    flower_turtle.forward(300)
    
    # Draw Leaf 
    flower_turtle.penup()
    flower_turtle.goto(0, -100)
    flower_turtle.setheading(280) 
    flower_turtle.pendown()
    flower_turtle.pensize(2)
    flower_turtle.color(stem_color)
    
    flower_turtle.begin_fill()
    flower_turtle.fillcolor(stem_color)
    flower_turtle.circle(100, 60) 
    flower_turtle.setheading(100) 
    flower_turtle.circle(100, 60) 
    flower_turtle.end_fill()

   
    flower_turtle.penup()
    flower_turtle.goto(0, petal_center_y - center_radius) 
    flower_turtle.pendown()
    flower_turtle.color(center_color)
    flower_turtle.begin_fill()
    flower_turtle.circle(center_radius)
    flower_turtle.end_fill()
    
   
    flower_turtle.penup()
    flower_turtle.goto(0, petal_center_y) 
    flower_turtle.pendown()
    flower_turtle.color(petal_color)
    flower_turtle.pensize(2)
    
 
    for _ in range(12):
        flower_turtle.begin_fill()
        flower_turtle.fillcolor(petal_color)
        flower_turtle.circle(petal_size, 90) 
        flower_turtle.left(90)
        flower_turtle.circle(petal_size, 90) 
        flower_turtle.end_fill()
        flower_turtle.left(180 - (360 / 12)) 


draw_real_flower(petal_color='magenta', center_color='gold', stem_color='green')

turtle.done()