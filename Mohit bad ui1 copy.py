'bad ui one. phone number'
'name Mohit'
'date april 24 2025'


from tkinter import messagebox, Tk, Label, Scale, HORIZONTAL, Button, Text
root = Tk()

label = Label(root,padx=10,pady=5,text='enter ur phone number',bg='red',fg='white')
label.grid(row=0)

scale = Scale(root,bg='blue',tickinterval=100000,resolution=1,orient=HORIZONTAL,from_=0,to=9999999999)

scale.grid(row=1,columnspan=500)


def submit1():
    thing=scale.get()
    messagebox.askyesno(message='is dis u fone num')
    text = Text(root,width=50,height=50,background='light blue')
    text.insert('1.0',thing)
    text.grid(row=2)
submit= Button(root,text='Submit',bg='purple',fg='white',command=submit1)
submit.grid(row=1,column=1)





root.mainloop()