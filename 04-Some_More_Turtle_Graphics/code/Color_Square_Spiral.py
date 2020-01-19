# draw a square spiral

import turtle

bob = turtle.Turtle()

colors = ["red", "yellow", "blue", "green"] 

for x in range(200):
    bob.color(colors[x%4])
    bob.forward(2*x)
    bob.left(91)
