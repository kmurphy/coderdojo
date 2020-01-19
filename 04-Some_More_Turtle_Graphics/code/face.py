import turtle

bob = turtle.Turtle()
bob.speed("fastest")

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def draw_circle(radius, color="black", fillcolor=None):
    bob.color(color)
    if fillcolor!=None:
        bob.fillcolor(fillcolor)
        bob.begin_fill()
    bob.circle(radius)
    if fillcolor!=None:
        bob.end_fill()
        

# face
jump(0,-150)
draw_circle(200, "yellow", "yellow")

# eyes
jump(-60,100)
draw_circle(15, "black", "black")
jump(60,100)
draw_circle(15, "black", "black")

# mouth
bob.width(15)
jump(-70,0)
 
bob.circle(100,100)
bob.hideturtle()
