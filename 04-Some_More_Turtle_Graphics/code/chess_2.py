import turtle

bob = turtle.Turtle()
size = 50
bob.speed("fastest")

bob.penup()
bob.goto(-200,-200)

def draw_square():
    bob.pendown()
    bob.begin_fill()
    for x in range(4):
        bob.forward(size)
        bob.left(90)
    bob.end_fill()
    bob.penup()


for c in range(8):
    for r in range(8):
        if (r+c)%2==0:
            bob.goto(-200+r*size, -200+c*size)
            draw_square()
        



    