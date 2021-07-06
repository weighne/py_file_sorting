from tkinter import *
from tkinter import filedialog
import os, sys
from pathlib import Path
from config import gui

# Definitions

top_level = Path("./")
font_settings = (gui['font'], gui['font_size'], gui['font_weight'])
dir = os.getcwd()

doc_ext = ['.doc','.docx','.pdf','.xls','.xlsx','.odt','.rtf','.txt','.ppt','.pptx','.odp','.ods','','']
pic_ext = ['.bmp','.gif','.jpeg','.jpg','.png','.svg','','','','','','','','']
audio_ext = ['.mp3','.wav','.wma','.ogg','.cda','.flac','.m4a','','','','','','','']
video_ext = ['.avi','.m4v','.mov','.mp4','.mpg','.mpeg','.wmv','','','','','','','']
code_ext = ['.py','.c','.cpp','.h','.java','.sh','.swift','.vb','.cs','.html','.css','.php','','']
zip_ext = ['.zip','.7z','.pkg','.rar','.rpm','.deb','','','','','','','','']
disk_ext = ['.dmg','.iso','.vcd','','','','','','','','','','','']
exe_ext = ['.exe','.apk','.bat','.jar','.msi','','','','','','','','','']
custom_ext = []
exts = [doc_ext, pic_ext, audio_ext, video_ext, code_ext, zip_ext, disk_ext, exe_ext]

# Functions

def browse_file():
    global dir
    dir = filedialog.askdirectory(initialdir=os.getcwd(),title="Select Directory")  # select target directory for sorting
    newpath_entry.insert(0,str(dir))  # update entry field
    print(dir)


def get_files():
    global dir
    print(dir)
    files = [x.path for x in os.scandir(dir) if x.is_file()]  # dump all the files within the directory into a list
    directories = [x.path for x in os.scandir(dir) if x.is_dir()]  # dump all subdirectories into a separate list
    print(*files, sep='\n')
    print(*directories, sep='\n')

    return files, directories


def submit():
    files, directories = get_files()

    for x in files:
        xsplit = x.split('.')
        extension = f".{xsplit[-1]}"
        print(extension)
        for y in exts:
            if extension in y:
                print(y)


# GUI

root = Tk()
root.title("Py File Sorting")

cpath_label = Label(root, text=f"Script Directory: {dir}")
cpath_label.configure(font = font_settings)
cpath_label.grid(columnspan=3,row=0,column=0,padx=5,pady=5)

newpath_label = Label(root, text="Custom Path: ").grid(row=1,column=0)
newpath_entry = Entry(root)
newpath_entry.grid(row=1,column=1,ipadx=100)
newpath_browse = Button(root, text="Browse...", command=browse_file).grid(row=1,column=2)

submit_button = Button(root, text="Submit", command=submit).grid(row=2,column=1)

root.update_idletasks()
root.mainloop()
