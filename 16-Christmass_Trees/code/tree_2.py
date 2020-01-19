# Starry Night Sky - www.101computing.net/christmas-tree/
import turtle
from turtle import *

from random import randint

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#00008C")

#let's draw the Moon
#draw_circle(myPen, "white", 120,80,50)
#draw_circle(myPen, "#00008C", 100,80,50)

#Let's add the Stars
numberOfStars = randint(6,12)
for star in range(0,numberOfStars):
  x = randint(-180,180)
  y = randint(-160,180)
  size = randint(5,20)
  #draw_star(myPen, "white", x, y, size)

#Add message to the card
myPen.penup()
myPen.color("yellow")
myPen.goto(-110, -180)
myPen.write("Season's Greetings", None, None, "24pt bold")
myPen.hideturtle()  
