from Tkinter import *
import ttk

root = Tk()

def key_press(event):
    print('copy')
root.bind('<Control-c>',key_press)


def press(event):
    print('Button is pressed')

imzoughene = ttk.Button(root,text='Click me')
imzoughene.bind('<ButtonPress>',press)
imzoughene.pack()


root.mainloop()