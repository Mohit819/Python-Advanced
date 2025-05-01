'''
Project: Screen Pet
Author:
Date

[Project Description]

'''

'''
TODO:
1. Copy over your screen pet drawing here to animate it! (Or you can make a new one if you wish)
2. Decide on at least 3 events and their corresponding actions
    EXAMPLES
    - Draw a set of closed eyes, and opened eyes. Pet blinks automatically. Pet winks if eyes clicked.
    - Draw an exaggerated smile. Pet switched mouth to smile if user moves mouse over face.
    - On activation (when window is created) Pet smiles / Any action
    - A pet's feature (ex. nose, ears) changes colour when clicked
'''

'''
HOW TO CREATE ALTERNATE VERSIONS:
1. Create a variable storing version 1, set state to NORMAL
2. Create a variable storing version 2, set state to HIDDEN
    This will create the object, but not place it on the screen.

HOW TO SWITCH BETWEEN THE VERSION:
1. Create a function that toggles
    1.1. Figure out which version is currently in use
        - do this using a global variable that keeps track of this OR
        - fetch the current state of the canvas object involved ex. if the variable for verson 1's state is HIDDEN (using c.itemcget function)
    1.2  Switch the state for the version in use to HIDDEN
    1.3  Switch the state for the other version to NORMAL - if using a global variable, change it now
2. Ensure this function is bound to the appropriate event
(EXAMPLE GIVEN - crossed and uncrossed version of eyes)

'''

'''
HOW TO MAKE ACTIONS OCCUR AUTOMATICALLY - TIMED
If you want func_a function to happen every second, in the function definition, write
root.after(1000, func_a) <- this tells the root to call this function again after 1000 milliseconds
Ensure function is called once in the main code.
(EXAMPLE GIVEN - crossing and uncrossing eyes is done automatically)

'''


from tkinter import *
root = Tk()

c = Canvas(root, width=500, height=500, bg='light blue')
crossed = False  # Starting out with uncrossed eyes

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
root.bind("<Button-1>", print_loc)









c.create_rectangle(30,30,570,570,fill = 'light blue',tags = 'background')
c.create_oval(150,150,450,450,fill="dark red", tags = "face")
c.create_polygon(394,181,462,171,414,205,fill = 'dark red',tags = "ear part 1,1")
c.create_polygon(459,173,428,220,417,203,fill = 'white',tags = "ear part 2,1")
c.create_polygon(197,192,145,158,182,206,fill = 'dark red',tags = "ear part 1,2")
c.create_polygon(182,206,145,158,167,231,fill = 'white',tags = "ear part 2,2")

c.create_oval(297,325,283,337,fill = 'pink',tags = 'nose')
mouth=c.create_line(246,385,290,347,335,378,fill = 'black',tags = 'mouth')
c.pack()





def toggle_eyes():
    '''
    If using a global variable, include lines like this to 
    use and check that variable

    global crossed
    if not crossed:
    '''
    # This function uses the approach of checking an object's state to determine what version is currently used
    if c.itemcget(left_eye_pupil_1, 'state') == NORMAL: #left_1 = normal, right1=normal, left_2 = hidden, right_2=hidden
        c.itemconfigure(left_eye_pupil_1, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_1, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_2, state=NORMAL)
        c.itemconfigure(right_eye_pupil_2, state=NORMAL)
        '''crossed = True # this is ESSENTIAL if using the global variable approach'''

    else:
        c.itemconfigure(left_eye_pupil_2, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_2, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_1, state=NORMAL)
        c.itemconfigure(right_eye_pupil_1, state=NORMAL)
        '''crossed = False'''

    # after 1000 milliseconds, call this function again
    root.after(1000, toggle_eyes)

left_eye_white = c.create_oval(241, 274, 283, 324, fill='white', tags=('eye'))
right_eye_white = c.create_oval(333, 275, 299, 322, fill='white', tags=('eye'))


# Normal pupils - the tags here haven't been used in this example but they may be helpful for other events
left_eye_pupil_1 = c.create_oval(255, 289, 268, 306, fill='black', tags=(
    'eye', 'pupil', 'uncrossed'), state=HIDDEN)
right_eye_pupil_1 = c.create_oval(322, 289, 311, 307, fill='black', tags=(
    'eye', 'pupil', 'uncrossed'), state=HIDDEN)

# Crossed eye pupils
left_eye_pupil_2 = c.create_oval(262, 298, 275, 317, fill='black', tags=(
    'eye', 'pupil', 'crossed'), state=NORMAL)
right_eye_pupil_2 = c.create_oval(314, 297, 305, 314, fill='black', tags=(
    'eye', 'pupil', 'crossed'), state=NORMAL)

toggle_eyes()  # function must be called once in the main code to start the automatic process



left_eyebrow = c.create_line(223,250,279,255,fill='black',tags='left eyebrow',state = NORMAL)
right_eyebrow = c.create_line(292,259,341,252,fill='black',tags='right eyebrow',state = NORMAL)



left_eyebrow_1 = c.create_line(237,225,283,263,fill='black',tags='angry left eyebrow',state=HIDDEN)
right_eyebrow_1 = c.create_line(337,227,298,266,fill='black',tags='angry right eyebrow',state=HIDDEN)


def angry_cat():
    if c.itemcget(left_eyebrow, 'state') == NORMAL: 
        c.itemconfigure(left_eyebrow, state=HIDDEN)
        c.itemconfigure(right_eyebrow, state=HIDDEN)

        c.itemconfigure(left_eyebrow_1, state=NORMAL)
        c.itemconfigure(right_eyebrow_1, state=NORMAL)


    else:
        c.itemconfigure(left_eyebrow_1, state=HIDDEN)
        c.itemconfigure(right_eyebrow_1, state=HIDDEN)

        c.itemconfigure(left_eyebrow, state=NORMAL)
        c.itemconfigure(right_eyebrow, state=NORMAL)
    root.after(1000,angry_cat)
angry_cat()



def smile(event):
    c.itemconfigure(mouth2,state=NORMAL)
    c.itemconfigure(mouth,state=HIDDEN)



mouth2 = c.create_line(252,347,290,379,340,342,fill='black',tags='smile',state=HIDDEN)

root.bind('<w>',smile)


def no_smile(event):
    c.itemconfigure(mouth2,state=HIDDEN)
    c.itemconfigure(mouth,state=NORMAL)


root.bind('<l>',no_smile)

c.pack()
root.mainloop()
