n = 100

import turtle

screen = turtle.Screen()

screen.tracer(0)

elfin = turtle.Turtle()

elfin.speed("fastest")

elfin.left(90)
elfin.forward(3*n)
elfin.color("orange", "yellow")
elfin.begin_fill()
elfin.left(126)
for i in range(5):
    elfin.forward(n/5)
    elfin.right(144)
    elfin.forward(n/5)
    elfin.left(72)
elfin.end_fill()
elfin.right(126)

elfin.color("dark green")
elfin.backward(n*4.8)
def tree(d, s):
    if d <= 0: return
    elfin.forward(s)
    tree(d-1, s*.8)
    elfin.right(120)
    tree(d-3, s*.5)
    elfin.right(120)
    tree(d-3, s*.5)
    elfin.right(120)
    elfin.backward(s)
    
tree(22, n)
elfin.backward(n/2)

screen.tracer(1,1)
import time
time.sleep(60)