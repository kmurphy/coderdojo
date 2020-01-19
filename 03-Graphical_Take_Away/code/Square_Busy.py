import turtle

window = turtle.Screen()
bob = turtle.Turtle()
bob.busy = False

def drawSquare():
    if bob.busy: return
    bob.busy = True
    
    for k in range(4):
        bob.forward(100)
        bob.left(90)
    bob.busy = False
        
window.onkey(drawSquare, "s")

window.listen()
window.mainloop()
