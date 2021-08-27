from tkinter import *
from tkinter import colorchooser # Submodule

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)

    
window = Tk()
window.title("Color Chooser")
window.geometry("420x420")

button = Button(window, text = "click me", command = click)
button.pack()

window.mainloop()