from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(initialdir="/home/ubuntu/PycharmProjects/Python_GUI/Sample-Files/",
                                          title="Open File",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files haha", "*.*")
                                          ))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text="open", command=openFile)
button.pack()

window.mainloop()