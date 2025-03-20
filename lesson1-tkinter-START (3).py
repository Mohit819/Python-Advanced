'''
Project Name:Screen Pet
Author:Mohit
Date:March 17, 2025

This is a title block! Title blocks help you keep track of the purpose and 
progress of a project. We will be including one at the beginning of all projects
from now on.

After filling out the 3 pieces of information, write a short blurb on 
what this project does and how to use it! This only needs to be two sentences
for this simple project.
It will make a pet using tkinter. It will make a background too.
'''


'''
TODO:
- create a canvas with a
    - background colour
    - size

- using lines, polygons, rectangles, and ovals, draw an animal on your canvas
- tag all your canvas objects!
'''




from tkinter import *
def print_loc(event):
    '''
    This function is made for you to help you get familiar with the grid on the
    screen!

    It will print out the X, Y coordinates of any point you want.
    When your program is running, simply click (using left mouse button)
    on the point on the canvas you want the location of.
    The output will be in the shell!

    '''
    print(event.x, event.y)


# Your window has been made for you below
root = Tk()


# this line allows our print function to be called when and wherever you click
root.bind("<Button-1>", print_loc)

# Create your canvas and all your canvas objects here! Don't forget to pack!
c = Canvas(root, height=600, width=600, bg='yellow')
# c.create_oval(150,150,450,450,fill="blue", tags = "face")
# c.create_polygon(371,169,426,127,420,210,fill = "red",tags = "ear1")
# c.create_polygon(215,173,171,129,185,201,fill="yellow",tags ="ear2")
# c.create_oval(203,197,231,248,fill = 'black',tags = "eye1")
# c.create_oval(349,189,369,228,fill = 'black',tags = "eye2")
# c.create_line(430,299,558,301,fill='black',tags = 'whisker1')
# c.create_line(426,321,554,328,fill='black',tags = 'whisker2')
# c.create_line(161,315,51,345,fill='black',tags = 'whisker3')
# c.create_line(163,343,56,380,fill='black',tags = 'whisker4')
# c.create_line(425,348,551,353,fill='black',tags = 'whisker5')
# c.create_line(172,363,69,409,fill='black',tags = 'whisker6')
# c.create_line(221,366,224,403,376,395,374,362,fill='black',tags = 'mouth')
c.create_rectangle(30,30,570,570,fill = 'light blue',tags = 'background')
c.create_oval(150,150,450,450,fill="dark red", tags = "face")
c.create_polygon(394,181,462,171,414,205,fill = 'dark red',tags = "ear part 1,1")
c.create_polygon(459,173,428,220,417,203,fill = 'white',tags = "ear part 2,1")
c.create_polygon(197,192,145,158,182,206,fill = 'dark red',tags = "ear part 1,2")
c.create_polygon(182,206,145,158,167,231,fill = 'white',tags = "ear part 2,2")
c.create_oval(248,285,289,336,fill = "white",tags ='eye part 1,1')
c.create_oval(266,311,281,328,fill = 'black',tags = 'eye part 2,1')
c.create_oval(337,286,294,337,fill = "white",tags ='eye part 1,2')
c.create_oval(317,311,302,326,fill = 'black',tags = 'eye part 2,2')
c.create_oval(297,325,283,337,fill = 'pink',tags = 'nose')
c.create_line(246,385,290,347,335,378,fill = 'black',tags = 'mouth')
c.pack()




# Do not remove this line! It keeps your window open while the code is running
root.mainloop()
