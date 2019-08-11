from Tkinter import *
import ttk

root = Tk()

def ClickMe(id):
    print('Button with Id : {} is clicked'.format(id))

#imzoughene = ttk.Button(root,text="click me",command=ClickMe)
#imzoughene.pack()

ttk.Button(root,text="click me",command=lambda : ClickMe(10)).pack()
root.mainloop()