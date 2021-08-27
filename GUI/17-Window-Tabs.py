from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook, text="Test Name")

tab1.pack()
notebook.pack()

window.mainloop()