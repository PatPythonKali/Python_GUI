from tkinter import *

# Widgets = GUI Elements : Buttons, Text Box, Labels, Images
# Windows = Serves as a container to hold or contain these widgets
window = Tk() # Instantiate an instance of a window
window.geometry("420x820") # Setting for window size
window.title("Youtube AI")

icon = PhotoImage(file = "/home/ubuntu/PycharmProjects/Python_GUI/Images/logo.png")
window.iconphoto(True, icon)
window.config(background="#050A30")

print(icon)

window.mainloop() # Place a window on the screen. Listens for events
