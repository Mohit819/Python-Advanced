'name ui'
'mohit rana'
'voting day'


from tkinter import *
root = Tk()


l = Label(root,text = 'yo yo yo enter yo name yo yo',bg='beige',fg='blue')
l.grid(row = 0, column=0)

name=StringVar()
e= Entry(root,textvariable=name)
e.grid(row=1,column=0)

b = Button(root,text='Submit')
b.grid(row=1,column=1)










root.mainloop()