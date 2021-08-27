from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="Info Message Box", message="You are a person")
    # messagebox.showwarning(title="Warning Message Box", message="You have a virus")
    # messagebox.showerror(title="Error Message Box", message="Something went wrong")
    result = messagebox.askyesnocancel(title="Ask Yes No Cancel", message="Yes no or cancel")
    if result == True:
        print("Yes was pressed")
    elif result == False:
        print("No was pressed")
    else:
        print("What the ?")

window = Tk()

button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()
