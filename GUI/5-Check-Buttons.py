from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree")

window = Tk()
window.title('Check Button')

x = BooleanVar()

check_button = Checkbutton(window,
                           text="I agree to the agreement.",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Ubuntu Mono", 12),
                           pady=10,

                           )
check_button.pack()

window.mainloop()