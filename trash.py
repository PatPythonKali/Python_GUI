from tkinter import *

window = Tk()
window.title("Fuck App")
window.geometry("420x720")
window.config(bg="black")

label = Label(window,
              text="Fuck",
              font=("Ubuntu Mono", 42),
              bg="black",
              fg="white",
              )
label.pack()

entry = Entry(window,
              text="submit",
              font=("Ubuntu Mono", 18),

              )
entry.pack()

button = Button(window,
                text="submit",
                padx=10,
                pady=10,
                )
button.pack()

window.mainloop()
