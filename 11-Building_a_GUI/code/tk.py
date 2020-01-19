import turtle
import tkinter as tk

def forward():
    t.forward(100)

def back():
    t.back(100)

def left():
    t.left(90)

def right():
    t.right(90)

root = tk.Tk()
canvas = tk.Canvas(master = root)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000") # Red
bob = turtle.RawTurtle(canvas)

tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)

root.mainloop()