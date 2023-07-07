# mi to km converter

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km = round(km, 2)
    kilometer_result_label.config(text=f"{km}")


# Create the window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=100, pady=40)

# Create the widgets
# Use a grid layout to place the widgets
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
