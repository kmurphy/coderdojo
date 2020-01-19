import turtle
window = turtle.Screen()
tree_maker = turtle.Turtle()
tree_maker.color("darkgreen")
# draw outline of tree
tree_maker.begin_fill()
tree_points = [[0, 400], [-200, 300], [-100, 300], [-300, 200], [-100, 200], [-400, 0], [400, 0], [100, 200], [300, 200], [100, 300], [200, 300], [0, 400]]
for tree_edge in tree_points:
    tree_maker.goto(tree_edge)
tree_maker.end_fill()
# draw trunk of tree
tree_maker.penup()
tree_maker.color("brown")
tree_maker.begin_fill()
trunk_points = [[100, 0], [-100, 0], [-100, -100], [100, -100], [100, 0]]
for each in trunk_points:
    tree_maker.goto(each)
tree_maker.end_fill()
# write a festive message
tree_maker.hideturtle()
tree_maker.goto(0, -200)
tree_maker.color("red")
tree_maker.write("Happy Holidays!", True, align="center", font=("Arial", 42, "normal"))
tree_maker.goto(0, -250)
tree_maker.write("See if you can decorate the tree!", True, align="center", font=("Arial", 18, "normal"))
# add your code below to decorate the tree!
window.mainloop()