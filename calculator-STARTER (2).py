'''
Calculator Builder - Starter Code
Author:Mohit
Date:April 3rd 2025

[Project Description]
its a calculator
'''
"""
TODO:
SETUP
1. Draw out your calculator on paper - think about what buttons should be included and how to arrange them
    MUST INCLUDE: 0,1,2,3,4,5,6,7,8,9,+,-,*,/, CLEAR, =, DEL (or DELETE or BACKSPACE)
    OPTIONAL: any buttons you choose, like on OFF button linked to root.quit()
2. From this drawing determine what row and column each button should be placed in
3. Pick out a colour-scheme so that your design is attractive

CODING
1. Create a Label that uses the 'expression' StringVar as its textvariable
2. Customize the CalcButton class so that creating your Buttons is easy and standardized
    2.1 Add more parameters to the __init__ function so your buttons can be created inside it
    2.2 Set the 'command' for your Buttons to be 'self.onClick' so that you can use the premade functions
3. Create a Label that uses the 'expression' StringVar as its textvariable - this is the top of the calculator where the expression appears
4. Create your Buttons using the CalcButton class. Some buttons you may want to create without it, especially if they have special commands.
    4.1 Your '=' button, for example, should have its command set to the 'evaluate' function instead
    4.2 Your 'CLEAR' button should have its command set to the 'clear' function

"""


from tkinter import *
root = Tk()
expression = StringVar()


class CalcButton():
    def __init__(self,frame ,char,bg_color,fg_color, row1,col1,command1=None):  # add extra parameters

        # this should be the character on the button, like '2' or '+' as a one character string
        self.char = char
        if command1==None:
            command1=self.onClick
            
        self.obj = Button(frame,text=char, bg=bg_color, fg=fg_color,command=command1)  # create your Button and store it as the 'obj' instance variable
        self.obj.grid(row= row1, column=col1)
        # are there any other pieces of information a button should store?

    def onClick(self):
        """
        This function simply adds this buttons character to the expression
        """
        expression.set(expression.get() + self.char)
    


def clear():
    """
    Clears the expression.
    """
    expression.set('')


def delete():
    """
    Removes the last character in expression.
    """
    expression.set(expression.get()[:-1])


def evaluate():
    """
    Calls the built-in function 'eval' which will evaluate a string according to Pythons evauation rules.
    Replaces the existing expression with the result of evaluating the expression.
    strip() removes any trailing whitespace (spaces or newline characters) since eval does not like them.
    Examples:
    eval('3+4') -> '7'
    eval('3 - 3 + 3 + 56') -> '59'              # spaces between numbers are optional
    eval('-2 * 6') -> '-12'                     # do not use 'x' for multiplication, must be '*'
    """
    
    try:
        result =str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("error")

# Create your frames and label here
main_frame = Frame(root,padx=10,pady=15,bg='black')
main_frame.grid(row=0,column=0)

numpad_frame = Frame(main_frame,padx=5,pady=5,bg='white')
numpad_frame.grid(row=6,column=10,rowspan=6,columnspan=10,sticky='s')

special_frame = Frame(main_frame,padx=1,pady=5,bg='white')
special_frame.grid(row=4,column=10,rowspan=1,columnspan=10)

entry_frame= Label(main_frame,padx=15,pady=5,textvariable=expression,bg='white',fg='blue')
entry_frame.grid(row=0,column=10,)
# Create your buttons here

CalcButton(numpad_frame,"1", "blue", "white",2,2)
CalcButton(numpad_frame,"2", "blue", "white",2,4)
CalcButton(numpad_frame,"3", "blue", "white",2,6)
CalcButton(numpad_frame,"4", "blue", "white",4,2)
CalcButton(numpad_frame,"5", "blue", "white",4,4)
CalcButton(numpad_frame,"6", "blue", "white",4,6)
CalcButton(numpad_frame,"7", "blue", "white",6,2)
CalcButton(numpad_frame,"8", "blue", "white",6,4)
CalcButton(numpad_frame,"9", "blue", "white",6,6)
CalcButton(numpad_frame,"0", "blue", "white",8,2)
CalcButton(numpad_frame,".", "blue", "white",8,4)
CalcButton(numpad_frame,"/", "blue", "white",2,8)
CalcButton(numpad_frame,"*", "blue", "white",4,8)
CalcButton(numpad_frame,"-", "blue", "white",6,8)
CalcButton(numpad_frame,"+", "blue", "white",8,8)

CalcButton(numpad_frame,"=", "blue", "white",8,6,command1=evaluate)
CalcButton(special_frame,"CLEAR", "blue", "white",2,2,command1=clear)
CalcButton(special_frame,"DEL", "blue", "white",2,8,command1=delete)

# Configure your rows and columns here as needed - remember to configure the root as well as your frames!

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)

for i in range(3):
    main_frame.rowconfigure(i,weight=1)
    main_frame.columnconfigure(i,weight=1)

for i in range(3):
    main_frame.rowconfigure(i,weight=1)
    main_frame.columnconfigure(i,weight=1)
    numpad_frame.rowconfigure(i,weight=1)
    numpad_frame.columnconfigure(i,weight=1)
    numpad_frame.columnconfigure(i,weight=1)
    numpad_frame.columnconfigure(i,weight=1)
    numpad_frame.columnconfigure(i,weight=1)
    numpad_frame.rowconfigure(i,weight=1)
    numpad_frame.rowconfigure(i,weight=1)
    numpad_frame.rowconfigure(i,weight=1)
for i in range(3):
    special_frame.rowconfigure(i,weight=1)
    special_frame.columnconfigure(i,weight=1)
    special_frame.columnconfigure(i,weight=1)

for i in range(3):
    entry_frame.rowconfigure(i,weight=1)
    entry_frame.columnconfigure(i,weight=1)
root.mainloop()
