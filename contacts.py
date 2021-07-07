from tkinter import *



top = Tk()
var = IntVar()

names = []
friends = []

def selectFriend():
    if (var.get()==1): print("You selected "+a.get()+" as a friend")
    friends.append(a.get())
    print("friends")
    print(friends)



L1 = Label(top,text="Name: ").grid(row=0,column=0)
a = StringVar()
E1 = Entry(top, bd=3, textvariable=a).grid(row=0,column=1)

R1 = Radiobutton(top, text = "Friend", variable = var, value = 1,command = selectFriend).grid(row=1,column=0)
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def addName():
    newname = a.get()
    #checks if name is valid or not
    if (newname == "")or(hasNumbers(newname)):
        print("Please enter a valid name")
    else:
        names.append(newname)
        print("contacts")
        print(names)




prC = Button(top,text="Add",command=addName)

prC.grid(row=2,column=0)


label = Label(top)
label.grid(row=3,column=0)

top.mainloop()

