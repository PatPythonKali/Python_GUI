from tkinter import *
window = Tk()

def submit():
    print(f"Hello {entry.get()} Fuck You!")
def clear():
    entry.delete(0, END)
def backspace():
    entry.delete(len(entry.get()) -1, END)

window.title("Entry")
window.geometry("420x720")

label = Label(window,
              font=("Ubuntu Mono", 24),
              text="Write Your Name Fucker!",
              fg="Black",
              pady = 18,
              )
label.pack()

entry = Entry(window,
              font=("Ubuntu Mono", 18),
              show="*",
              )
entry.pack()

submit_btn = Button(window,
                    text="submit",
                    command=submit,
                    )
submit_btn.pack(side=TOP)

clear_btn = Button(window,
                   text="clear",
                   command=clear,
                   )
clear_btn.pack(side=TOP)

backspace_btn = Button(window,
                       text="backspace",
                       comman=backspace,
                       )
backspace_btn.pack()

window.mainloop()