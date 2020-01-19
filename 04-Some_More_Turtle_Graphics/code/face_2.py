import turtle

screen = turtle.Screen()
bob = turtle.Turtle()
bob.speed("fastest")

bob.busy = False
bob.asleep = True

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
def open_eyes():
    jump(-60,100)
    draw_circle(15, "black", "black")
    jump(60,100)
    draw_circle(15, "black", "black")
open_eyes()

def close_eyes():
    jump(-60,105)
    draw_circle(15, "yellow", "yellow")
    jump(60,105)
    draw_circle(15, "yellow", "yellow")
close_eyes()

# mouth
bob.width(15)
jump(-70,0)
bob.setheading(-50)
bob.color("black")
bob.circle(100,100)


def wakeup(x,y): 
    bob.asleep = False
    open_eyes()
    pass

def sleep(x,y): 
    bob.asleep = True
    close_eyes()
    pass
        
screen.onclick(wakeup)

turtle.onrelease(sleep)


screen.listen()
screen.mainloop()