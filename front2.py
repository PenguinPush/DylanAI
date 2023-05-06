import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

color = {"white": "#FFEAEC"}

root = ctk.CTk()
root.title("i want to fucking die")
root.geometry("800x600")

def login():
    print("Test")

c=0

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Macro list:", text_color="#FFEAEC", font=("nexa bold", 30))
label.pack(pady=(40,20), padx=30)

scroll = ctk.CTkScrollableFrame(master=frame,corner_radius=20, fg_color="#3C3744", width=600, height=300,scrollbar_button_color="#817A90",scrollbar_button_hover_color="#FFEAEC")
scroll.pack(pady=(20,0), padx=0)

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    y.configure(text="File Opened: "+filename)
    

def add(a):
    global c
    
    y=ctk.CTkEntry(scroll,fg_color="#817A90",placeholder_text="Name",placeholder_text_color="#FFEAEC",font=("nexa bold", 20),border_width=0)
    y.pack(side=ctk.LEFT,pady=10, padx=10,fill=ctk.BOTH, expand=True)

    x=ctk.CTkButton(scroll,fg_color="#817A90",text="Choose file",text_color="#FFEAEC",font=("nexa bold", 20),border_width=0,state="readonly",command = browseFiles)
    x.pack(side=ctk.LEFT,pady=10, padx=20,fill=ctk.BOTH, expand=True)

    z = ctk.CTkCheckBox(scroll)
    z.pack(padx=(0,10), pady=10)

    return c + 1

add(c)

add = ctk.CTkButton(root, fg_color="#3C3744", text="add",font=("nexa bold",20),text_color="#FFEAEC")
add.pack(side=ctk.LEFT, padx=200, pady=(10,30), fill=ctk.BOTH, expand=True)

root.mainloop()