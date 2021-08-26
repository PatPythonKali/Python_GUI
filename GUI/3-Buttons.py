from tkinter import *
counter = 0
def ClickButton():
    global counter
    counter += 1
    print(f"Button was clicked {counter} times!")

window = Tk()
window.title("Buttons")
window.geometry("420x420")

buttons = Button(window,
                 text = "Click Me!",
                 padx = 10,
                 pady = 10,
                 command = ClickButton,
                 )
buttons.pack()

window.mainloop()