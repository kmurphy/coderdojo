from turtle import Turtle
import random
 
bob=Turtle()
bob.screen.bgcolor("black")
bob.speed(0)

def random_drawing(turns,distance):
    for x in range(turns):
        right = bob.right(random.randint(0,360))
        left = bob.left(random.randint(0,360))
        bob.color(random.choice(["blue","red","green"]))
        
        random.choice([right,left])
        bob.fd(distance)
        if bob.gety()<-300:
            print ("below")
            bob.penup()
            bob.y += 600
            bob.penup()
        if bob.y>-300:
            print ("Above")
            bob.penup()
            bob.y -= 600
            bob.penup()
 
 
random_drawing(1000,50)