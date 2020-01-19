import turtle

bob = turtle.Turtle()
size = 50
bob.speed("fastest")

bob.penup()
bob.goto(-200,-200)

def square_and_move():
    bob.pendown()
    bob.begin_fill()
    for x in range(4):
        bob.forward(size)
        bob.left(90)
    bob.end_fill()
    bob.penup()
    bob.forward(2*size)

for r in range(4):
    for k in range(4):
        square_and_move()
    bob.left(90)
    bob.forward(size*2)
    bob.left(90)
    for k in range(4):
        square_and_move()
    bob.right(180)


    