'''
To-Do List App - STARTER
Author:mohit
Date:may 5

[Project Description]
todo list app to use
'''

'''
TODO:
1. Draw out your app on paper! Choose a colourscheme and your widget arrangement.
2. Set up your window and create your frames. (under class definitions)
3. Fill out the Classes, following the commented instructions

    Classes and other outlines are just suggestions! If you find it more complicated
    to follow this structure than make your own - go ahead and make your own or change
    the classes here!

4. Configure rows and columns (under frame and label creation)
5. Modify layout to make it look nice!
6. Test it out!
    - Ensure that progress bar resizes with window
    - Ensure that progress bar is accurate (should be 2/3 full if there are 3 items, 2 checked off)
7. Clean up your code! Check to make sure all your instance variables are actually necessary, etc.

'''

'''
EXTRAS THAT WILL BE HELPFUL:

root.winfo_width() <- returns current width of the window
[Canvas].winfo_width() <- returns current width of chosen Canvas
winfo_height() will do the same for current height
'''


from tkinter import *
root = Tk()
root.title('To-Do List')
root.geometry('500x500')
root.resizable(True,True)

# Configure root here, give it a title, start size, resizability, etc.
NUM_ITEMS=0
NUM_DONE=0

class ProgressBar():
    def __init__(self,bg,fg):
        '''
        Customize this with the info needed to make your progress bar!
        self.canvas ,create rectangle, canvas.grid
        '''
        self.c=Canvas(pink_guy,height=100,width=250,bg=bg)
        self.bar=self.c.create_rectangle(0,0,0,0,fill=fg,tags='w')
        self.c.grid(row=4,column=0,columnspan=2)

    def resize(self,event):
        unit_size= self.c.winfo_width()//NUM_ITEMS
        new_width= unit_size * NUM_DONE
        self.c.coords(self.bar,0,0,new_width,self.c.winfo_height())
        '''
        winfo_width is to get width of progress bar
        An additional method could be useful for updating the progress bar
        when a new item is added or an item is checked/unchecked.

        This method can also handle the resizing necessary when the window
        changes size, or you can handle that seperately.

        '''

        


class ListItem():
    '''
    Items of this class are the entire line in your To-Do List.
    They contain the Entry (for the user to type their list item),
    the Checkbutton (created once Entry is destroyed),
    and can contain your Trashcan Button if you choose to make one.
    '''

    def __init__(self,r):
        # Set up any instance attributes here
        global todo_man
        self.r=r
        # Create a StringVar for your Entry, give it some default text
        # Create a StringVar for your Checkbutton, empty
        # Create an IntVar for your Checkbutton (to keep track of its state)
        self.i=StringVar(value='Enter todo item here')
        self.g=StringVar()
        self.j=IntVar()

        
        # Create your Checkbutton   <- Could do this in replace_entry instead if you want
        self.check = Checkbutton(todo_man,textvariable=self.i,command=self.checkbox_update,variable=self.j,onvalue=1,offvalue=0)
        # Grid your Checkbutton     <-
        self.check.grid(row=r,column=0)
        self.e=Entry(todo_man,textvariable=self.i,text=self.i)
        self.e.grid(row=r,column=0)
        # Handle event binding
        root.bind('<Return>',self.replace_entry)
        root.bind('<ButtonPress>',self.clear_entry)
        # - when Entry clicked -> default text should disappear
        
        
        # - when User is using Entry and hit Return Button -> Entry should disappear and be replaced with Checkbutton
        # - when Checkbutton is checked/unchecked -> progress bar should update
        
        # May need to do some row configuration here, since each ListItem is on a new row

    def clear_entry(self, event):
        '''
        Clears the default text out of the Entry
        '''
    
        
        self.i.set('')

    def replace_entry(self,event):
        '''
        Destroys Entry and replaces with Checkbutton
        '''
        global NUM_ITEMS
        NUM_ITEMS +=1
        self.e.destroy()
        self.trashy=PhotoImage(file='Python Advanced/trashcan.png')
        self.trash=Button(todo_man,image=self.trashy,command=self.delete,bg='light blue')
        self.trash.grid(row=self.r,column=1)
        ListItem(self.r+1)

    def delete(self):
        global NUM_DONE
        global NUM_ITEMS
        if self.g.get():
            NUM_DONE -= 1
        self.check.destroy()
        self.trash.destroy()
        NUM_ITEMS-=1
            


    def checkbox_update(self):
        '''
        Update required variables when boxes are checked/unchecked, trigger progress bar change.
        '''
        global NUM_DONE
        if self.j.get() == 1:
            NUM_DONE+=1
            pb.resize(None)
        else:
            NUM_DONE -=1
            pb.resize(None)

# Create basic necessary Frames
todo_man = Frame(root,height=500,width=500,bg='light blue')
todo_man.grid(row=5,column=1)
pink_guy=Frame(root,height=100,width=500,bg='light pink')
pink_guy.grid(row=7,column=1)
# Create Labels
todoMan=Label(root,padx=10,pady=1,text='TO DO:',bg='gray',fg='black',font=('Times New Roman',10))
todoMan.grid(row=0,column=1)
pro=Label(pink_guy,text='Progress Bar',bg='gray',fg='black',font=('Times New Roman',10))
pro.grid(row=0,column=0)
pb=ProgressBar("white", "black")
root.bind('<Configure>',pb.resize)

# Create first ListItem

# Create Canvas to hold ProgressBar and ProgressBar

# Configure rows and columns - for the root, and each frame as necessary!
ListItem(0)

root.mainloop()










