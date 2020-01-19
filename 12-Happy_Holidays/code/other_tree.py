from turtle import *
from random import randint

width = 500
height = 600
setup(width, height, "Happy Christmas from CoderDojo Tramore!")


BG_COLOR = "#0080ff"

screen.bgcolor(BG_COLOR)

y = -100

create_rectangle(-15, y-60, 30, 60, 'red', 'red')

# create tree
width = 240
oogway.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(oogway, "green", x, y, width, height)
    y = y + height

# create a star a top of tree
oogway.speed(1)
oogway.penup()
oogway.color('yellow')
oogway.goto(-20, y+10)
oogway.begin_fill()
oogway.pendown()
for i in range(5):
    oogway.forward(40)
    oogway.right(144)
oogway.end_fill()

tree_height = y + 40

# create moon in sky
# create a full circle
create_circle(oogway, 230, 180, 60, "white")
# overlap with full circle of BG color to make a crescent shape
create_circle(oogway, 220, 180, 60, BG_COLOR)

# now add few stars in sky
oogway.speed(10)
number_of_stars = randint(20,30)
# print(number_of_stars)
for _ in range(0,number_of_stars):
    x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5,20)
    oogway.penup()
    oogway.color('white')
    oogway.goto(x_star, y_star)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(size)
        oogway.right(144)
    oogway.end_fill()

# print greeting message
oogway.speed(1)
oogway.penup()
msg = "Merry Christmas from ThePythonDjango.Com"
oogway.goto(0, -200)  # y is in minus because tree trunk was below x axis
oogway.color("white")
oogway.pendown()
oogway.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

oogway.hideturtle()
screen.mainloop()

