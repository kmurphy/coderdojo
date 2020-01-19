# This is a Python program that uses two modules, the turtle and tkinter modules.
# When a module is used in Python you need to import it into your program.
import turtle
import tkinter

# Next, the main function is defined. Defining a function doesn't do anything other 
# than tell Python the name of the function. Next the program jumps all the way down 
# to the "if" statement at the bottom of the file.
def main():
   
   # Here is the first line of the main function's code. 
   root = tkinter.Tk()
   root.title("Draw!")
   cv = tkinter.Canvas(root,width=600,height=600)
   cv.pack(side = tkinter.LEFT)
   
   # This is how we create a turtle to draw on the canvas we created above.
   t = turtle.RawTurtle(cv)
   screen = t.getscreen()
   
   # With the lines below, the "turtle" will look like a pencil.
   #screen.register_shape("pencil.gif")
   #t.shape("pencil.gif")

   # This sets the lower left corner to 0,0 and the upper right corner to 600,600. 
   screen.setworldcoordinates(0,0,600,600)
   screen.bgcolor("white")

   # A frame is an invisible widget that holds other widgets. This frame goes 
   # on the right hand side of the window and holds the buttons and Entry widgets.
   frame = tkinter.Frame(root)
   frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)

   pointLabel = tkinter.Label(frame,text="Width")
   pointLabel.pack()
   
   # This entry widget allows the user to pick a width for their lines. 
   # With the pointSize variable below you can write pointSize.get() to to 
   # the contents of the entry widget and pointSize.set(val) to set the value
   # of the entry widget to val. Initially the pointSize is set to 1. str(1) is needed because
   # the entry widget must be given a string.
   pointSize = tkinter.StringVar()
   pointEntry = tkinter.Entry(frame,textvariable=pointSize)
   pointEntry.pack()
   pointSize.set(str(1))
   
   # This is an event handler. Handling the quit button press results in destroying the window
   # and quitting the application. 
   def quitHandler():
      root.destroy()
      root.quit() 
      
   # This is how a button is created in the frame. The quitHandler is the event handler for button
   # presses of the "Quit" button.
   quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
   quitButton.pack()
   
   # Here is another event handler. This one handles mouse clicks on the screen.
   def clickHandler(x,y): 
      # When a mouse click occurs, get the pointSize entry value and set the width of the 
      # turtle called "t" to the pointSize value. The int(pointSize.get()) is needed because
      # the width is an integer, but the entry widget stores it as a string.
      t.width(int(pointSize.get()))
      t.goto(x,y)
      
   # Here is how we tie the clickHandler to mouse clicks.
   screen.onclick(clickHandler)
   
   # Finally, this code is last. It tells the application to enter its event processing loop
   # so the application will respond to events. 
   tkinter.mainloop()
   
# Python jumps right here after executing the def main() line. These two lines tell 
# Python to jump to the first line of the main function above. Seems a little strange,
# but there are good reasons for this which you'll learn if you take some computer 
# science.
if __name__ == "__main__":
   main()