import turtle

bob = turtle.Turtle()
bob.speed("fastest")
bob.left(180)

colors = ["red", "yellow", "green", "blue", "white"]

for x in range(len(colors)):
    bob.color(colors[x])
    bob.fillcolor(colors[x])
    size = 400-x*80
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()