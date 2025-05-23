from tkinter import *
from numpy.ma.core import left_shift

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)     #modifying the widgets from the margins of the window

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)     #easy way to place labels and buttons where we want on the screen
                                    #no need to call again pack, they don't work together
my_label.config(padx=100, pady=100)

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop() # code that will keep the Tkinter on screen. This code needs to be at the bottom of the code