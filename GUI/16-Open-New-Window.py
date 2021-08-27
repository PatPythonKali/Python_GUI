from tkinter import *

def newWindow():
    new_window = Toplevel()
    # new_window = Tk()

    window.destroy()


window = Tk()
window.title("Open New Window")

Button(window, text="open new window", command=newWindow).pack()

window.mainloop()