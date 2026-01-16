import turtle

def draw_colorful_spiral(initial_len):
    screen = turtle.Screen()
    screen.bgcolor("black") 
    spiral_turtle = turtle.Turtle()
    spiral_turtle.speed(0) 
    
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    
    current_len = initial_len
    
   
    for i in range(150):
        
        spiral_turtle.pencolor(colors[i % 6])
        
       
        spiral_turtle.forward(current_len)
        
        
        spiral_turtle.right(91) 
        
        
        current_len += 2 

    spiral_turtle.hideturtle()
    screen.mainloop()


draw_colorful_spiral(initial_len=5)