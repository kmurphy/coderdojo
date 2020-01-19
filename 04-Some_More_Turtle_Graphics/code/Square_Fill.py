import turtle

bob = turtle.Turtle()

bob.color("red")
bob.fillcolor("blue")

bob.begin_fill()
bob.width(4)
for x in range(4):
    bob.forward(100)
    bob.left(90)
bob.end_fill()
    