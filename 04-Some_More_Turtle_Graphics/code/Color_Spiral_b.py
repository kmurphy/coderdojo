# draw any spirals

import turtle

bob = turtle.Turtle()
bob.speed("fastest")

window = turtle.Screen()
window.bgcolor("black")

# pick between 2 and 6 sides
sides = 3 

colors = ["red", "yellow", "blue", 
    "orange", "green", "purple"]

for x in range(360):
    bob.color(colors[x%sides])
    bob.forward(x * 3/sides + x)     
    bob.left(360/sides + 1)
    bob.width(x*sides/200)