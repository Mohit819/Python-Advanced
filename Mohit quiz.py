'''
Project Title: Personal Quiz
Author:Mohit
Date:Monday, March 24, 2025

[insert description of project and instructions for use]

'''


'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''


from tkinter import *
root = Tk()
c = Canvas(root, height = 600,width=600,bg = 'white')
c.pack()
# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []

result = StringVar()


def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

# Add all your questions and widgets here




question1=StringVar()
f = Frame(c,height=400,width=400,bg="red")
f.pack()
l = Label(f,text='what is 8 * 8?',bg='white',fg='black',justify='center')
l.pack()
r1 = Radiobutton(f,text='16',variable=question1, value="16")
r2 = Radiobutton(f,text='54',variable=question1,value='54')
r3 = Radiobutton(f,text='64',variable=question1,value='64')
r1.pack()
r2.pack()
r3.pack()
answers.append('64')
stringvars.append(question1)

question2=StringVar()
f2=Frame(c,height=400,width=400,bg="orange")
f2.pack()
l2=Label(f2,text='who is the current prime minister of Canada?',bg='white',fg='black',justify='center')
l2.pack()
r21 = Radiobutton(f2,text='Justin Trudeau',variable=question2, value="Justin Trudeau")
r22 = Radiobutton(f2,text='Mark Carney',variable=question2,value='Mark Carney')
r23 = Radiobutton(f2,text='Pierre Poilievre',variable=question2,value='Pierre Poilievre')
r21.pack()
r22.pack()
r23.pack()
answers.append('Mark Carney')
stringvars.append(question2)

question3=StringVar()
f3=Frame(c,height=400,width=400,bg="yellow")
f3.pack()
l3=Label(f3,text='Is this spelt correctly,"Pneumonoultramicroscopicsilicovolcanoconiocis"',bg='white',fg='black',justify='center')
l3.pack()
r31=Radiobutton(f3,text='Yes',variable=question3,value='Yes')
r32=Radiobutton(f3,text='No',variable=question3,value='No')
r31.pack()
r32.pack()
answers.append('No')
stringvars.append(question3)

question4 = StringVar()
f4=Frame(c,height=400,width=400,bg="green")
f4.pack()
l4=Label(f4,text='Is ThermoFlask a water brand or a oil brand?')
l4.pack()
r41=Radiobutton(f4,text="water brand",variable=question4,value='water brand')
r42=Radiobutton(f4,text="oil brand",variable=question4,value='oil brand')
r41.pack()
r42.pack()
answers.append('water brand')
stringvars.append(question4)

question5=StringVar()
f5=Frame(c,height=400,width=400,bg="blue")
f5.pack()
l5=Label(f5,text='Apple is a______')
l5.pack()
r51 = Radiobutton(f5,text='none of the below',variable=question5,value='none of the below')
r52 = Radiobutton(f5,text='fruit',variable=question5,value='fruit')
r53 = Radiobutton(f5,text='company',variable=question5,value='company')
r54 = Radiobutton(f5,text='all of the above',variable=question5,value='all of the above')
r51.pack()
r52.pack()
r53.pack()
r54.pack()
answers.append('all of the above')
stringvars.append(question5)
# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!

results = Label(root, textvariable=result)
results.pack()

root.mainloop()
