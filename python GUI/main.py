from Tkinter import *
import ttk
root = Tk()
button = ttk.Button(root,text='imzoughene')
button.pack()
def buClick():
    print('imzoughene is a great person')
    
button.config(command=buClick)
#button.invoke()
#button.state(['disabled']) # disable the button
#button.state(['!disabled']) # enable the button
#button.instate(['disabled']) # check if button is disabled = false
root.mainloop()