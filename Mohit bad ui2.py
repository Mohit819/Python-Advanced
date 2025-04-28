'birthday'
'mohit'
'april 24 2025'

from tkinter import *
root=Tk()

label = Label(root,padx=10,pady=5,text='enter ur birthdate. month date year',bg='red',fg='white')
label.grid(row=0)

scale = Scale(root,bg='dark blue',tickinterval=10000000,resolution=1,orient=VERTICAL,from_=10101,to=12312026)
scale.grid(row=1)

def submit1():
    thing=scale.get()
    text = Text(root,width=50,height=50,background='red')
    text.insert('1.0',thing)
    text.grid(row=2)

submit= Button(root,text='Submit',bg='purple',fg='white',command=submit1)
submit.grid(row=1,column=1)













root.mainloop()