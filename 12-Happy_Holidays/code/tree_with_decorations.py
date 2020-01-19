from my_library import *

width = 200
height = 600
setup(width, height, "Happy Christmas from CoderDojo Tramore!")

# start drawing

# my functions

def snow_fall():
    rate_of_snow_balls = 3
    rand_make_snow = random.randint(0, rate_of_snow_balls)
    if rand_make_snow == 0:
        snow = turtle.Turtle()
        snow.shape('circle')
        snow.color('white')
        snow.shapesize(.3)
        snow.right(90)
        snow.penup()
        
        snow_drops.append(snow)
        x = random.randint(-width / 2, width / 2)
        y = width / 2
        snow.setposition(x,y)
        
    for snow in snow_drops:
        move_snow(snow)
        if snow.ycor() <= -width / 2:
            snow.clear()
            snow_drops.remove(snow)
            del snow
    screen.update()

def move_snow(snow):
    snow_speed = 2
    snow.forward(snow_speed)


#screen.tracer(0)
#draw_rectangle(0, 0, 100, 50, None, 'black')
#draw_triangle(0, 0, 100, 50)

screen.bgcolor("sky blue")
bob.hideturtle()

screen.tracer(0)

# draw trunk
draw_rectangle(-width/30, -height/3, width/15, height/2, 'black', 'brown')

# draw tree
bob.pensize(10)
color = 'black'
fill_color = None
for k in range(2):
    draw_triangle(0, 0.33*height, 0.33*width, 0.18*height, color, fill_color)
    draw_triangle(0, 0.25*height, 0.5*width, 0.25*height, color, fill_color)
    draw_triangle(0, 0.125*height, 0.66*width, 0.33*height, color, fill_color)
    color = None
    fill_color = 'forest green'

# draw ground
bob.pensize(1)
draw_rectangle(-width/2, -height/2, width, 0.18*height, 'white', 'white')

# draw star
draw_star(0,height/3+15, 20, 'yellow', 'yellow')

# draw decorations
decorations = [ (-0.1, 0.05,'red'), (0, 0,'violet') ]

for x,y,c in decorations:
    draw_ball(width*x,height*y, 8,c,c)

# snow 
snow_drops = []

jump(0, height / 2.7)
bob.color("red")
bob.write("Merry Christmas",
    font=("Apple Chancery", 30, "bold"), align="center")

for k in range(50):
    snow_fall()
    

jump(-width/4, -0.4*height)
bob.write("from",
    font=("Apple Chancery", 20, "normal"), align="center")

for k in range(25):
    snow_fall()
    
bob.color("forest green")
jump(0, -0.45*height)
bob.write("CoderDojo", font=("Avenir", 30, "normal"),
             align="center")

for k in range(25):
    snow_fall() 
jump(0.3*width, -0.45*height)
bob.color("black")
bob.write("Tramore", font=("Avenir", 30, "normal"),
             align="center")

bob.hideturtle()
#  

  
while True:
    snow_fall()

turtle.done()