import turtle

bob = turtle.Turtle()
size = 50
bob.speed("fastest")

bob.color("blue")

n = 36
for k in range(n):
    bob.circle(100)
    bob.left(360/n)