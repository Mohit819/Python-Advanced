'''
Paint App Project
Author:me
Date:05 29

[Project Description]
 paint
'''

from tkinter import *

''''
Your window has been created for you.
TODO:
- create your frame
- create your canvas

'''
root = Tk()
root.title('Paint')
menu=Frame(root,bg='light grey',)
menu.grid(row=0,column=0,sticky='n')
c=Canvas(root,height=1000,width=1000,bg='white')

'''
This project will use some global variables.
COLOUR represents the current colour being used, and
SIZE is the current size of the paintbrush.
'''
COLOUR = 'black'
SIZE = 10

class ColourButton():

     '''
     A ColourButton is the class for the buttons at the
     top of the screen that change the brush colour.
     '''
     def __init__(self, colour):
          global menu
          global COLOUR
          global SIZE
          '''
          This is the function called when creating a ColourButton.
          TODO:
          - fill in the line indicated below.
          '''
          self.colour = colour
          self.Button =Button(menu,bg=colour,command=self.update) #FILL IN
     def update(self):

          '''
          This is the method that is the command for a ColourButton.

          When a ColourButton is pressed, it must ONLY change the global COLOUR
          variable to be this ColourButton's colour attribute/
          TODO:
          - fill in this function. It should be 2 lines.
          '''
          global COLOUR
          COLOUR = self.colour
     
def draw_circle(event):
    '''
    This function is called whenever the user is dragging their mouse on the
    canvas. Use the canvas method 'createoval' to draw a circle there.
    Remember to refer to your global variables to draw the correct circle.
    TODO:
    - finish this function (should be 1-2 lines)
    '''
    global c
    global COLOUR
    c.create_oval(event.x,event.y,event.x+SIZE.get(),event.y+SIZE.get(),fill=COLOUR,outline=COLOUR)
def clear_canvas():
    '''
    This function is called whent the user presses the CLEAR button.
    It must clear all drawings from the canvas.
    TODO:
    - finish this function (1 line)
    '''
    c.delete('all')

#################### MAIN CODE #########################

'''
Here we first are making the ColourButtons. We will do this in a quick
and expandable way using a list. Add all the colours you want buttons for
to the list 'colours'.
The for loop will create the ColourButton objects.
TODO:
- add at least 4 more colours to the colours list
'''

colours = ['red', 'orange','yellow','green','blue','purple','pink','black']
for i in range(len(colours)):
    x = ColourButton(colours[i])
    x.Button.grid(row=0, column=i)

'''
Next create the CLEAR button and the width slider.

TODO:
- complete the code fragments below
'''
clear_button = Button(menu,text='CLEAR',command=clear_canvas)# FILL IN
clear_button.grid(row = 0, column = i + 1)

SIZE = IntVar() # We are using the global variable as the int var so it is always updated
scalebar =Scale(menu,variable=SIZE,tickinterval=1,resolution=1,from_=1,to=10,orient=HORIZONTAL) # Fill in - there are many ways to do this
scalebar.grid(row = 0, column = i + 2)

'''
TODO:
- bind the event of mouse button held down while moving ON THE CANVAS to the draw_circle function
- bind the letter q to quitting the program
- mainloop!
'''
root.bind('<q>',root.quit())
c.bind('<B1-Motion>',draw_circle)
c.grid(row=1,column=0,sticky='news')
root.mainloop()