from tkinter import *
from tkinter import filedialog
import os, sys
from pathlib import Path
from config import gui

# Definitions

top_level = Path("./")
font_settings = (gui['font'], gui['font_size'], gui['font_weight'])
dir = os.getcwd()

# Functions

def browse_file():
    global dir
    dir = filedialog.askdirectory(initialdir=os.getcwd(),title="Select Directory")
    newpath_entry.insert(0,str(dir))
    print(dir)

def get_files():
    global dir
    print(dir)
    files = [x.path for x in os.scandir(dir) if x.is_file()]
    #list(os.scandir(dir))
    print(*files, sep='\n')

# GUI

root = Tk()
root.title("Py File Sorting")

cpath_label = Label(root, text=f"Current Directory: {os.getcwd()}")
cpath_label.configure(font = font_settings)
cpath_label.grid(columnspan=3,row=0,column=0,padx=5,pady=5)

newpath_label = Label(root, text="Custom Path: ").grid(row=1,column=0)
newpath_entry = Entry(root)
newpath_entry.grid(row=1,column=1,ipadx=100)
newpath_browse = Button(root, text="Browse...", command=browse_file).grid(row=1,column=2)

submit_button = Button(root, text="Submit", command=get_files).grid(row=2,column=1)

root.update_idletasks()
root.mainloop()
