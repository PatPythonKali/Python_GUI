from tkinter import *


def radio_button_press():
    if x.get() == 0:
        print("Pizza")
    elif x.get() == 1:
        print("Hamburger")
    elif x.get() == 2:
        print("Hotdog")

def clear_screen():
    quit()


food = ["Pizza", "Hamburger", "Hotdog"]
print(food)
window = Tk()
window.title("GUI Buttons")

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               command=radio_button_press,
                               padx = 25,
                               font=("Ubuntu Mono", 18),
                               indicatoron=0
                               )
    radio_button.pack(anchor=W)

button_clear = Button(window,
                      text="clear",
                      command=clear_screen,
                      )
button_clear.pack()

window.mainloop()
