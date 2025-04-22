from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")

miles_input = Entry()
miles_input.grid(column = 1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid

kilometer_result_label = Label(text="0")

kilometer_label = Label(text="Km")

calculate_button = Button("Calculate")

window.mainloop()