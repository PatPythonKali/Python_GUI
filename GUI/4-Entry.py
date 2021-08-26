from tkinter import *
window = Tk()

def submit():
    username = entry.get()
    print(type(entry))
    print("Hello " + username)

def clear():
    entry.delete(0, END)


window.title = "Entry"

entry = Entry(window,
              font = ("Ubuntu Mono", 50)
              )
entry.pack()

submit_button = Button(window,
                text = "submit",
                command = submit)
submit_button.pack(side = RIGHT)

clear_button = Button(window,
                 text = "clear",
                 command = clear)
clear_button.pack(side = RIGHT)

window.mainloop()