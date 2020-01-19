import turtle

bob = turtle.Turtle()

def drawPolygon(n):
    angle = 360/n
    for k in range(n):
        bob.forward(100)
        bob.left(angle)


bob.color("red")
drawPolygon(4)
bob.color("green")
drawPolygon(5)
bob.color("blue")
drawPolygon(9)
