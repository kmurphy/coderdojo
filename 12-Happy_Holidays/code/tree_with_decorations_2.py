from my_library import *

w = 500
h = 600
setup(w, h, "Happy Christmas from CoderDojo Tramore!")

# ### my data ###
screen.tracer(0)
# ### my functions ###

# ### my drawings ###

# draw background
screen.bgcolor("sky blue")
#bob.hideturtle()

# draw trunk
draw_rectangle(-0.02*w, -0.3*h, 0.04*w, 0.5*h, 'black', 'brown')

# draw tree
bob.pensize(10)
draw_triangle(0, 0.33*h, 0.33*w, 0.18*h, 'black')
draw_triangle(0, 0.25*h, 0.50*w, 0.25*h, 'black')
draw_triangle(0, 0.12*h, 0.66*w, 0.33*h, 'black')
draw_triangle(0, 0.33*h, 0.33*w, 0.18*h, None, 'forest green')
draw_triangle(0, 0.25*h, 0.50*w, 0.25*h, None, 'forest green')
draw_triangle(0, 0.12*h, 0.66*w, 0.33*h, None, 'forest green')
  
# draw ground
bob.pensize(1)
draw_rectangle(-w/2, -h/2, w, 0.2*h, 'white', 'white')

# draw star
draw_star(0,0.33*h+15, 20, 'yellow', 'yellow')

# draw decorations
decorations = [ (-0.1, 0.05,'red'), (0, 0,'violet') ]

for x,y,c in decorations:
    draw_ball(w*x,h*y, 8,c,c)

# draw message - Merry Christmas
jump(0, 0.4*h)
bob.color("red")
font = ("Apple Chancery", 30, "bold")
bob.write("Merry Christmas", font=font, align="center")

# draw snow falling (for a short while)

# draw message - from
jump(-0.25*w, -0.4*h)
font = ("Apple Chancery", 20, "normal")
bob.write("from", font=font, align="center")

# draw snow falling (for a short while)

# draw message - CoderDojo
bob.color("forest green")
jump(0, -0.45*h)
font = ("Avenir", 30, "normal")
bob.write("CoderDojo", font=font, align="center")

# draw snow falling (for a short while)

# draw message - Tramore
jump(0.3*w, -0.45*h)
bob.color("black")
bob.write("Tramore", font=font, align="center")

# draw snow falling ... forever ....
