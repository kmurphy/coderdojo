# draw any spirals

import turtle
import sys

bob = turtle.Turtle()
bob.speed("fastest")

screen = turtle.Screen()
sx, sy = screen.screensize()
print (sx,sy)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
print (sx,sy)


print (dir(screen))


screen.bgcolor("black")

def quit():
    print("quit")
    screen.bye()
    sys.exit(1)
    
def finish_drawing():
    screen.tracer(0)

screen.onkey(quit, "q")
screen.onkey(finish_drawing, "f")
screen.listen()

# pick between 2 and 6 sides
sides = 6 

colors = ["red", "yellow", "blue", 
    "orange", "green", "purple"]

for x in range(360):
    bob.color(colors[x%sides])
    bob.forward(x * 3/sides + x)     
    bob.left(360/sides + 1)
    bob.width(x*sides/200)

screen.tracer(1)

turtle.mainloop()

