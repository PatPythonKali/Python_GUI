from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All Files", ".*")
                                    ])
    filetext = textbox.get(1.0, END)
    file.write(filetext)
    file.close()

window = Tk()
window.title("File Save")

textbox = Text(window, bg="Light Yellow")
textbox.pack()

button = Button(window, text="save", command=saveFile)
button.pack()



window.mainloop()