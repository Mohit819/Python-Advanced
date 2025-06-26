#NAME MOHIT
#DESCRIPTION: it a math quiz but more importantly FINAL TKINTER PROJECT
#DATE 06/12/2025
from tkinter import colorchooser,Frame,Tk,Menu,Label,Button,Entry,StringVar,IntVar,messagebox
import random as r
root=Tk()

question_frame=Frame(root,height=600,width=600,bg='light gray')
top_label=Label(root,text='This is a Math Multiplication Quiz')
question_frame.grid(row=1,column=0)
top_label.grid(row=0,column=0)
menubar = Menu(root)
menu_file = Menu(menubar) 
menu_edit = Menu(menubar)
menu_run = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
menubar.add_cascade(menu=menu_run, label='Run')
menu_file.add_command(label='New')
menu_file.add_command(label='Open...')
menu_file.add_command(label='Close')
root.config(menu = menubar)


user_num=IntVar(value='')
def question():
    global inte
    num1=r.randrange(0,12)
    num2=r.randrange(0,12)
    thing=[num1,'*',num2]
    thing2=(num1*num2)
    que=Label(text=thing)
    que.grid(row=3,column=0)    
    inte = thing2
    return thing2
def colour():
    rgb, hex = colorchooser.askcolor()
    COLOUR=hex
    question_frame.configure(bg=COLOUR)
def get2():
    global correct
    global wrong
    global user_num
    if user_num.get() == inte:
        correct += 1
        print("Correct: " + str(correct))
    else:
        wrong+=1
        print(inte)
        print("Wrong:" + str(wrong))
    if correct+wrong==5:
        messagebox.showinfo(message='you got %s wrong and %s correct'%(wrong,correct))
        root.quit()
    question()
    delete()
def delete():
    user_num.set('')

correct=0
wrong=0
submit=Button(question_frame,text='Submit',command=get2)
submit.grid(row=4,column=0)
entry=Entry(question_frame,textvariable=user_num)
entry.grid(row=1,column=0)
col=Button(question_frame,text='Choose bg colour',command=colour)
col.grid(row=3,column=0)
inte=question()
root.mainloop()