import random
import turtle

coins = 10
startCoinCount = 21

wn = turtle.Screen()

def drawCoins():
    turtle.tracer(0, 0)
    turtle.clear()
    
    # find size of bottom row
    total = 0
    rowLength = 1
    while total<startCoinCount:
        total = total + rowLength
        rowLength = rowLength + 1
    
    # draw remaining coins
    toDraw = coins
    y = 0
    x = -rowLength*2
    turtle.penup()
    while toDraw>0:
        drawCoin()
        turtle.setposition(x,y)
        x = x + 100
        toDraw = toDraw - 1
    turtle.update()       
        

def drawCoin():
    turtle.shape("circle")
    turtle.shapesize(1,2)
    turtle.stamp()
    
    
wn.onkey(drawCoins, "s")


wn.listen()

