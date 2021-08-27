from tkinter import *

window = Tk()
window.title("Frames")

frame = Frame(window, bg="Pink", bd=5, relief=SUNKEN)
frame.pack(side=BOTTOM)

Button(frame, text="W", font=("Consolas", 25), widt=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame,text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()