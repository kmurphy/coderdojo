my_library_version = 0.1

import turtle
import random

# create our screen
def setup(width, height, title):
    "Create screen to start"
    screen.setup(width, height, startx=0, starty=0)
    screen.title(title)


def jump(x,y):
    "Move to position (x,y) without leaving a trail."
    bob.remember_pen = bob.isdown()   
    bob.penup()
    bob.setposition(x,y)
    bob.pen(pendown=bob.remember_pen)


def begin_draw(x,y, color, fill_color):
    "Helper function to start drawing a shape."
    
    jump(x, y)
    
    bob.remember_pen = bob.isdown()
    
    if color:
        bob.pendown()
        bob.color(color)
    else:
        bob.penup()
        
    if fill_color:
        bob.fillcolor(fill_color)
        bob.begin_fill()


def end_draw(x,y, color, fill_color):
    "Helper function to end drawing a shape."
    if fill_color:
        bob.end_fill()
    bob.pen(pendown=bob.remember_pen)


def draw_ball(x, y, radius, color='black', fill_color=None):
    """Draw a ball (disk) at position (x,y) and radius (radius),
    draws outline edge with color (color), or no edge if None (default black),
    fills shape with color (fill_color), or no fill in None (default None)."""
    begin_draw(x,y,color,fill_color)
    bob.circle(radius)
    end_draw(x,y,color,fill_color)
    
    
def draw_rectangle(x, y, width, height, color='black', fill_color=None):
    """Draw a rectangle with bottom left corner at (x,y) and width (width) and height (height),
    draws outline edge with color (color), or no edge if None (default black),
    fills shape with color (fill_color), or no fill in None (default None)."""
    begin_draw(x,y,color,fill_color)       
    for k in range(2):
        bob.forward(width)
        bob.left(90)
        bob.forward(height)
        bob.left(90)
    end_draw(x,y,color,fill_color)       


def draw_triangle(x, y, base, height, color='black', fill_color=None):
    """Draw an isosceles triangle with top corner at (x,y) and base (base) and height (height),
    draws outline edge with color (color), or no edge if None (default black),
    fills shape with color (fill_color), or no fill in None (default None)."""
    begin_draw(x,y,color,fill_color)
    bob.goto(x-base/2, y-height)
    bob.goto(x+base/2, y-height)
    bob.goto(x,y)
    end_draw(x,y,color,fill_color) 


def draw_star(x, y, size, color='black', fill_color=None):
    """Draw a star with top corner at (x,y) and size (size),
    draws outline edge with color (color), or no edge if None (default black),
    fills shape with color (fill_color), or no fill in None (default None)."""
    begin_draw(x,y,color,fill_color)

    bob.left(288)
    for i in range(5):
        bob.forward(size)
        bob.right(144)
    bob.right(288)
    end_draw(x,y,color,fill_color) 

if __name__=="__main__":
    print("Don't run me!")
else:
    screen = turtle.Screen()
    bob = turtle.Turtle()

    