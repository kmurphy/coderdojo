import turtle

bob = turtle.Turtle()

size = 500
bob.speed("fastest")

for k in range(size):
    bob.forward(k)
    bob.left(101)
    
    # mix a new color
    f = k/size   # number between 0 and 1
    myColor = (f, 1-f, f*f)
    
    bob.color(myColor)
  