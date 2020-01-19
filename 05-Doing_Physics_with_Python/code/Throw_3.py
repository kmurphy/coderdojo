# setup physics problem
y = 1.3
v = 25
a = -9.81
t = 0

dt = 0.01
output_dt = 0.01

max_height = 0

import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-5,-5,5,45)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(0.5)

ball.penup()
ball.goto(0,y)
ball.pendown()

# print header
print("%12s %12s %12s" % ("time", "height", "velocity"))
print("="*39)

# do computation
while True:
    
    if abs(int(t/output_dt)-t/output_dt)<dt:
        print("%12.3f %12.2f %12.2f" % (t, y, v))

    ball.goto(0,y)

    y = y + v*dt
    v = v + a*dt
    t = t + dt
    
    if y<0: break
    
# output final data
print("The ball was in the air for %.2f seconds." % t)
print("At impact ball was moving at %.2f metres per second." % -v)
print("Maximum height of ball was %.2f metres." % max_height)
