from tkinter import *
count = 1
def click():
    global count
    count += 1
    print(f"You Clicked the button {count - 1} times!")

window = Tk()

button = Button(window,
                text = "click me",
                command=click,
                font = ("Ubuntu Mono", 20),
                bg = "black",
                activebackground = "black",
                fg = "green"
                )
button.pack()

window.mainloop()