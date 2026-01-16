import turtle
import math

def draw_shiva_lingam_final(color='gray30', base_color='gray', mark_color='red'):
    screen = turtle.Screen()
    screen.setup(width=600, height=800)
    screen.bgcolor("lightyellow") 
    
    lingam_turtle = turtle.Turtle()
    lingam_turtle.speed(0) 
    lingam_turtle.hideturtle()
    lingam_turtle.pensize(2)
    BASE_Y = -250       
    BASE_WIDTH = 240
    BASE_HEIGHT = 20
    DISC_WIDTH = 300
    DISC_HEIGHT = 40
    LINGAM_WIDTH = 80
    LINGAM_HEIGHT = 180
    LINGAM_RADIUS = LINGAM_WIDTH / 2 
    def draw_rectangle(width, height, fill_color, start_y):
        lingam_turtle.penup()
        lingam_turtle.goto(-width / 2, start_y)
        lingam_turtle.pendown()
        lingam_turtle.fillcolor(fill_color)
        lingam_turtle.pencolor(fill_color)
        lingam_turtle.begin_fill()
        for _ in range(2):
            lingam_turtle.forward(width)
            lingam_turtle.left(90)
            lingam_turtle.forward(height)
            lingam_turtle.left(90)
        lingam_turtle.end_fill()
        return start_y + height 
    current_y = draw_rectangle(BASE_WIDTH, BASE_HEIGHT, base_color, BASE_Y)
    current_y = draw_rectangle(DISC_WIDTH, DISC_HEIGHT, color, current_y)
    current_y = draw_rectangle(LINGAM_WIDTH, LINGAM_HEIGHT, color, current_y)
    

    lingam_turtle.penup()
    lingam_turtle.goto(0, current_y) 
    lingam_turtle.fillcolor(color)
    lingam_turtle.pencolor(color)
    lingam_turtle.dot(LINGAM_WIDTH, color) 

    
    mark_y = current_y + (LINGAM_RADIUS / 2) 
    
    lingam_turtle.penup()
    lingam_turtle.pencolor('white')
    lingam_turtle.pensize(2)
    
    
    line_spacing = 6
    line_length = LINGAM_WIDTH * 0.45 
    
    for i in range(3):
        
        lingam_turtle.goto(-line_length / 2, mark_y + (i * line_spacing) - line_spacing)
        lingam_turtle.pendown()
        lingam_turtle.forward(line_length)
        lingam_turtle.penup()

    
    lingam_turtle.goto(0, mark_y + (line_spacing * 3) + 3) 

    
    screen.mainloop()


draw_shiva_lingam_final()