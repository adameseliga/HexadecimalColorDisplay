# Simple reflexive AI agent

import tkinter as tk
from tkinter import messagebox

def evaluatecolor(): # Input: hexadecimal value passed into the entry box
                    # i.e. Actuator
    try:
        hex_val = e1.get() # <-- input

        frame.config(bg = hex_val)# Changes the pre-configured frame to the color of the hexadecimal

    except: # Triggers message if the value entered is not a valid hexadecimal value
        # i.e. Performance Measure
        tk.messagebox.showinfo(title = "Invalid Hexadecimal Value",
                               message = "Enter a valid hexadecimal value \n"
                                         "Example: #ff0000")



HEIGHT, WIDTH = 400, 400

# Create the root window in which the program runs
# i.e. Environment
root = tk.Tk()
root.geometry(f"{HEIGHT}x{WIDTH}")
root.title("Hexadecimal Color Identifier")
root.eval("tk::PlaceWindow . center")

label = tk.Label(root,
                 text='Enter a hexadecimal value (e.g.#ff0000, #F12A41)\n'
                      'to see its color representation below.',
                 font = ("Ariel", 12),
                 padx = 20,
                 pady = 20
                 )
label.pack()

e1 = tk.Entry(root) # Entry box
e1.pack()

enter_button = tk.Button(root, # Enter button
                         text = "Enter",
                         command = evaluatecolor)
enter_button.pack()

frame = tk.Frame(root, # Color display
                 height=100,
                 width=100,
                 relief="raised")
frame.pack()



if __name__ == '__main__':
    root.mainloop()
