from Tkinter import *
import ttk

root = Tk()

input = ttk.Entry(root,width=70)
input.pack()

button = ttk.Button(root,text='Click me')
button.pack()

def buClick():
    print(input.get())
    input.delete(0,END)
    #input.delete(0,3)
    input.insert(0,'Button clicked')


button.config(command=buClick)

root.mainloop()