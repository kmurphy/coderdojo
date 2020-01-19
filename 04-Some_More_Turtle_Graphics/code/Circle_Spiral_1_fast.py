# draw a square spiral

import turtle

bob = turtle.Turtle()
bob.speed("fastest")

for x in range(200):
    bob.circle(x)
    bob.left(90)
