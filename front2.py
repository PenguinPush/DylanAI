import customtkinter as ctk
import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import filedialog
filename = " "
trigger=[]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

color = {"white": "#FFEAEC"}

root = ctk.CTk()
root.title("HI FIRENDS")
root.geometry("800x600")

def login():
    print("Test")

c=0  # amount of inputs given

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Macro list:", text_color="#FFEAEC", font=("nexa heavy", 30))
label.pack(pady=(40,20), padx=30)

scroll = ctk.CTkScrollableFrame(master=frame,corner_radius=20, fg_color="#3C3744", width=600, height=300,scrollbar_button_color="#817A90",scrollbar_button_hover_color="#FFEAEC")
scroll.pack(pady=(20,0), padx=0)

def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
<<<<<<< HEAD
                                                        "*.*")))  
        x.configure(text=Path(filename).stem)
        return filename

def add():
    global c, filename
    
    frame=ctk.CTkFrame(scroll,fg_color="#3C3744")
    frame.pack(pady=5,fill=ctk.X, expand=True)

    x=ctk.CTkButton(frame,fg_color="#817A90",text=filename,text_color="#FFEAEC",font=("nexa bold", 20),border_width=0,state="readonly",command = browseFiles,anchor="w")
=======
                                                        "*.*")))
      
    # Change label contents
    y.configure(text="File Opened: "+filename)

def add():
    global c
    
    y=ctk.CTkEntry(scroll,fg_color="#817A90",placeholder_text="Name",placeholder_text_color="#FFEAEC",font=("nexa heavy", 20),border_width=0)
    y.pack(side=ctk.LEFT,pady=10, padx=10,fill=ctk.BOTH, expand=True)
    y.pack(pady=10, padx=10,fill=ctk.X, expand=True)

    x=ctk.CTkButton(scroll,fg_color="#817A90",text="Choose file",text_color="#FFEAEC",font=("nexa heavy", 20),border_width=0,state="readonly",command = browseFiles)
>>>>>>> a18bbcd6921680ba477bfd9ff926344125ff7529
    x.pack(side=ctk.LEFT,pady=10, padx=20,fill=ctk.BOTH, expand=True)

    y=ctk.CTkEntry(frame,fg_color="#817A90",placeholder_text="Name",placeholder_text_color="#FFEAEC",text_color="#FFEAEC",font=("nexa bold", 20),border_width=0)
    y.pack(side=ctk.LEFT,pady=10, padx=10,fill=ctk.BOTH, expand=True)

    z = ctk.CTkCheckBox(frame,fg_color="#817A90", text="Run!",font=("nexa bold",20),text_color="#FFEAEC",border_color="#817A90",checkbox_height=30,
                        checkbox_width=30,border_width=4,hover_color="#817A90",onvalue=1,offvalue=0)
    
    for i in range(c):
        if z.get() == 1:
            trigger.append(1)
        else:
            trigger.append(0)

<<<<<<< HEAD
    z.pack(padx=(10,0), pady=10)

    print(trigger)

    c+=1 # counter +1

    return frame

add = ctk.CTkButton(root, fg_color="#3C3744", text="add",font=("nexa bold",20),text_color="#FFEAEC",command=add)
add.pack(side=ctk.LEFT, padx=200, pady=(10,30), fill=ctk.BOTH, expand=True)
=======
add_button = ctk.CTkButton(root, fg_color="#3C3744", text="add",font=("nexa heavy",20),text_color="#FFEAEC", command=add)
add_button.pack(side=ctk.LEFT, padx=200, pady=(10,30), fill=ctk.BOTH, expand=True)
>>>>>>> a18bbcd6921680ba477bfd9ff926344125ff7529

root.mainloop()