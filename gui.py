from tkinter import *
import os, sys
from pathlib import Path
from config import gui

# Definitions

top_level = Path("./")
font_settings = (gui['font'], gui['font_size'], gui['font_weight'])

# Functions



# GUI

root = Tk()
root.title("Py File Sorting")

path_label = Label(root, text=f"Current Directory: {os.getcwd()}")
path_label.configure(font = font_settings)
path_label.grid(row=0,column=0)

root.update_idletasks()
root.mainloop()
