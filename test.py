from tkinter import *
# Label = An area WIDGET that holds text and/ or an image within a window
window = Tk()

photo = PhotoImage(file='./Images/logo.png')

# window.geometry("420x820")
window.config(background="#050A30")
window.geometry("420x720")
window.title("Test App")
label = Label(window,
              text = "Fuck",
              font = ("Ubuntu Mono", 45, "bold"),
              fg = 'white',
              bg = '#050A30',
              relief = RAISED,
              bd = 10,
              padx=20,
              pady=20,
              image=photo,
              compound = "top")
label.pack()
# label.place(x=0, y=0)

window.mainloop()