import turtle

window = turtle.Screen()

bob = turtle.Turtle()

def drawSquare():
    for k in range(4):
        bob.forward(100)
        bob.left(90)
        
window.onkey(drawSquare, "s")

window.listen()
window.mainloop()
