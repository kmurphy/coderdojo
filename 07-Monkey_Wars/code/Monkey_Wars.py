import turtle
import math
import random

screen = turtle.Screen()
screen.setup (width=600, height=600, startx=0, starty=0)
screen.setworldcoordinates(-300,-10,300,500)

WINDOW_WIDTH = 25
FLOOR_HEIGHT = 40

bob = turtle.Turtle()     # draws the city
red = turtle.Turtle()     # red player
blue = turtle.Turtle()    # blue player

def jump(t, x,y):
    t.penup()
    t.setposition(x,y)
    t.pendown()
 
     
def draw_rectangle(x,y, width, height, color="black"):
    
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

#draw_rectangle(100,0,50,100)

def draw_building(x,y, windows, floors, color="black", health=1):

    height = floors*FLOOR_HEIGHT
    width  = windows*WINDOW_WIDTH
    print ("Building with %d floors and %d windows per floor"
           % (floors, windows))
    
    draw_rectangle(x,y, width, height, color=color);
    
    for floor in range(floors):
        for window in range(windows):
            color = "yellow" if random.random()<health else "black"
            draw_rectangle(x+(0.3+window)*WINDOW_WIDTH,
                y + (0.3+floor)*FLOOR_HEIGHT,
                WINDOW_WIDTH*0.4, FLOOR_HEIGHT*0.4, color) 


red = turtle.Turtle()
blue = turtle.Turtle()

def draw_city():
    screen.tracer(0)
   
    red.floors = random.randint(2,10)
    red.health = 1

    blue.floors = random.randint(2,10)
    blue.health = 1

    draw_building(-300,0,3,red.floors , "red", red.health)
    draw_building(-50,20,3,11, "gray")
    draw_building(-150,20,10,9, "gray")
    draw_building(-225,0,5,6)
    draw_building(0,10,7,3, "darkgray")
    draw_building(90,0,5,4)
    draw_building(215,0,3, blue.floors, "blue", 0.1)

    screen.tracer(1,1)

draw_city()

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

def redUp():
    red.left(2)
    print ("Player red heading is now %s" % red.heading())
    
def redDown():
    red.right(2)
    print ("Player red heading is now %s" % red.heading())

def redFire():
    print ("Player red fired")
    fire(red)
    
def blueUp():
    blue.left(2)
    print ("Player blue heading is now %s" % blue.heading())
    
def blueDown():
    blue.right(2)
    print ("Player blue heading is now %s" % blue.heading())

def blueFire():
    print ("Player blue fired")
    fire(blue)

def fire(player):
    pass
    
    # create a new turtle to represent the rock
    screen.tracer(0)
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.shapesize(0.5)
    
    # move rock to player position and heading
    x, y = player.position()
    jump(ball, x, y)
    
    # use projectile logic to get vertical and horizontal speed
    speed = 100
    dt = 0.05
    angle = math.pi/180*player.heading()
    dx = speed*math.cos(angle)
    dy = speed*math.sin(angle)
    
    # animate rock movement
    screen.tracer(1)
    while 1:

        # update rock position
        x = x + dx*dt
        y = y + dy*dt
        dy = dy - dt*9.81
        ball.goto(x,y)
        
        # check if rocks moved passed city
        if x<-300 or x>300 or y<0: break
        
        # check if collision with buildings
        
        # check if passed screen

    ball.clear()
    
screen.onkey(redUp, "q")
screen.onkey(redDown, "a")
screen.onkey(redFire, "z")  
screen.onkey(blueUp, ".")
screen.onkey(blueDown, ",")
screen.onkey(blueFire, "m")

screen.listen()
screen.mainloop()