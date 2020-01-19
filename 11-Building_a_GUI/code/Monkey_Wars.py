import turtle
import math, sys
import random

# setup world

screen = turtle.Screen()
screen.setup (width=600, height=600, startx=0, starty=0)
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
screen.setworldcoordinates(-500,-10,500,800)

WINDOW_WIDTH = 25
FLOOR_HEIGHT = 40

bob = turtle.Turtle()     # draws the city
bob.hideturtle()
red = turtle.Turtle()     # red player
blue = turtle.Turtle()    # blue player

from collections import namedtuple
Building = namedtuple("Building", "x y w h color windows")
bob.buildings = [] 

def jump(t, x,y):
    t.penup()
    t.setposition(x,y)
    t.pendown()


def drawRectangle(x,y, width, height, color="black"):
    
    jump(bob,x,y)

    bob.color(color)
    bob.begin_fill()
    bob.setheading(0)
    bob.forward(width)
    bob.left(90)
    bob.forward(height)
    bob.left(90)    
    bob.forward(width)
    bob.left(90)
    bob.forward(height)
    bob.left(90)
    bob.end_fill()


def drawBuilding(x,y, windows, floors, color="black", health=100):

    height = floors*FLOOR_HEIGHT
    width  = windows*WINDOW_WIDTH
    windowCount = 0
    
    drawRectangle(x,y, width, height, color=color);
    
    for floor in range(floors):
        for window in range(windows):
            if random.random()<health/100:
                windowColor = "yellow"
                windowCount = windowCount + 1
            else:
                windowColor = "black"
            drawRectangle(x+(0.3+window)*WINDOW_WIDTH,
                y + (0.3+floor)*FLOOR_HEIGHT,
                WINDOW_WIDTH*0.4, FLOOR_HEIGHT*0.4, windowColor)
    
    print ("Building with %2d floors and %2d windows per floor (%2d working)"
           % (floors, windows, windowCount))

    return Building(x,y, width, height, color, windowCount)
            
            
def drawCity():
    screen.tracer(0)
    random.seed(bob.seed)

    bob.buildings = [
        drawBuilding(-300,0,3,red.floors , "red", red.health),
        drawBuilding(-50,20,3,11, "gray"),
        drawBuilding(-150,20,10,9, "gray"),
        drawBuilding(-225,0,5,6),
        drawBuilding(0,10,7,3, "darkgray"),
        drawBuilding(90,0,5,4),
        drawBuilding(215,0,3, blue.floors, "blue", blue.health)
    ]


def startGame():
    # to make same windows break duwing a game 
    bob.seed = random.randint(1,10000)
    
    red.floors = random.randint(2,10)
    red.health = 100

    blue.floors = random.randint(2,10)
    blue.health = 100

    drawCity()

    jump(red,-280,red.floors*FLOOR_HEIGHT+10)
    red.setheading(90)
    red.shape("triangle")
    red.shapesize(0.5)
    red.color("red")

    jump(blue,270,blue.floors*FLOOR_HEIGHT+10)
    blue.setheading(90)
    blue.shape("triangle")
    blue.shapesize(0.5)
    blue.color("blue")

    red.firing = False
    blue.firing = False
    screen.tracer(1)
    

# commands


def quit():
    screen.bye()
    sys.exit()


def redUp():
    red.left(2)
    print ("Player red heading is now %s" % red.heading())


def redDown():
    red.right(2)
    print ("Player red heading is now %s" % red.heading())


def redFire():
    if blue.firing or red.firing: return
    print ("Player red fired")
    fire(red)
 
 
def blueUp():
    blue.left(2)
    print ("Player blue heading is now %s" % blue.heading())
 
 
def blueDown():
    blue.right(2)
    print ("Player blue heading is now %s" % blue.heading())


def blueFire():
    if blue.firing or red.firing: return
    print ("Player blue fired")
    fire(blue)


def fire(player):
    
    
    if not player.firing:
        
        # create a new turtle to represent the rock
        screen.tracer(0)
        player.ball = turtle.Turtle()
        player.ball.shape("circle")
        player.ball.shapesize(0.5)
    
        # move rock to player position and heading
        x, y = player.position()
        jump(player.ball, x, y)
    
        # use projectile logic to get vertical and horizontal speed
        speed = 100
        dt = 0.1
        angle = math.pi/180*player.heading()
        dx = speed*math.cos(angle)
        dy = speed*math.sin(angle)
    
        # animate rock movement
        screen.tracer(1)
        player.firing = True

    while player.firing:

        # update rock position
        x = x + dx*dt
        y = y + dy*dt
        dy = dy - dt*9.81
        player.ball.goto(x,y)
        
        # check if rocks moved passed city
        if x<-300 or x>300 or y<0:
            player.firing = False
            break
        
        # check if collision with buildings
        for b in bob.buildings:
            if (b.x<x<b.x+b.w) and (b.y<y<b.y+b.h):
                print ("Hit building %s" % b.color)
                if b.color=='red':
                    hit = red
                elif b.color == 'blue':
                    hit = blue
                else:
                    hit = None
                
                if hit is not None:
                    hit.health = (hit.health//20)*10
                    print ("Player %s health drops to %s" % (b.color, hit.health))
                    drawCity()
                    if hit.health==0:
                        jump(bob,0,600 + 100*(b.color=="red"))
                        bob.color("black")
                        bob.write("Player %s lost." % b.color, align="center", font=("Comic Sans", 90, "normal"))
                
                player.firing = False
                break       

    player.ball.clear()

startGame()

screen.onkey(quit, "q")

screen.onkey(redUp, "a")
screen.onkey(redDown, "z")
screen.onkey(redFire, "x")

screen.onkey(blueDown, ".")
screen.onkey(blueUp, ",")
screen.onkey(blueFire, "m")

screen.listen()


screen.mainloop()
