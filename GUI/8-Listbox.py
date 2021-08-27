def submit():
    print("You have ordered: "+listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

from tkinter import *
window = Tk()
window.title("List Box")

label = Label(window)
label.config(text="List Box")
label.config(font=("Ubuntu Mono", 47))
label.pack()

listbox = Listbox(window,
                  bg="white",
                  font=("Ubuntu Mono", 28)
                  )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()



window.mainloop()