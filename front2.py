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
root.geometry("800x700")

c=0  # amount of inputs given

barTop = tk.Frame(root, bg="#3C3744", height=50)
barTop.pack(side="top", fill=tk.X)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

menuState = False

menuOpenImage = PhotoImage(file="menuOpen.png")
menuCloseImage = PhotoImage(file="menuClose.png")

def switch():
    global menuState
    if menuState is True:
        for b in range(301):
            menuFrame.place(x=-b, y=0)
            barTop.update()

       
        barTop.config(bg="#3C3744")
        root.config(bg="#242424")

        menuState = False
    else:
       
        barTop.config(bg="#3C3744")
        root.config(bg="#242424")

        for b in range(-300, 0):
            
            menuFrame.place(x=b, y=0)
            barTop.update()

        menuState = True


def hi():
    print("e")


topBar = tk.Button(barTop, image=menuOpenImage, bg="#3C3744", activebackground="#3C3744", bd=0, padx=20, command=switch)
topBar.place(x=10, y=10)



menuFrame = tk.Frame(root, bg="#242424", height=1000, width=300)
menuFrame.place(x=-300, y=0)
tk.Label(menuFrame, font="Bahnschrift 15", bg="#817A90", fg="#3C3744", height=2, width=300, padx=20).place(x=0, y=-4)

y = 80
options = ["Menu", "Dylan", "Help"]
def button(a,x,y,cmd):

    def invert_colors(event):
        bg = but.cget("bg")
        fg = but.cget("fg")
        but.config(background=fg, foreground=bg)

    but = tk.Button(menuFrame, text=options[a], font=("nexa bold", 30), bg="#3C3744", fg="#817A90", activebackground="#3C3744", activeforeground="#FFEAEC", bd=0,command=cmd,anchor=tk.CENTER, width=9)
    but.place(x=x, y=y)
    but.bind("<Enter>", invert_colors)
    but.bind("<Leave>", invert_colors)



button(0,35,80,hi())
button(1,35,190,hi())
button(2,35,300,hi())




menuClose = tk.Button(menuFrame, image=menuCloseImage, bg="#817A90", bd=0, command=switch)
menuClose.place(x=250, y=10)

label = ctk.CTkLabel(master=frame, text="Macro list:", text_color="#FFEAEC", font=("nexa bold", 30))
label.pack(pady=(40,20), padx=30)

scroll = ctk.CTkScrollableFrame(master=frame,corner_radius=20, fg_color="#3C3744", width=600, height=300,scrollbar_button_color="#817A90",scrollbar_button_hover_color="#FFEAEC")
scroll.pack(pady=(20,40), padx=0)

def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files","*.*")))  
        x.configure(text=Path(filename).stem)
        return filename

def add():
    global c, filename
    
    frame=ctk.CTkFrame(scroll,fg_color="#3C3744")
    frame.pack(pady=5,fill=ctk.X, expand=True)

    x=ctk.CTkButton(frame,fg_color="#817A90",text=filename,text_color="#FFEAEC",font=("nexa bold", 20),border_width=0,state="readonly",command = browseFiles,anchor="w")
    x.pack(side=ctk.LEFT,pady=10, padx=20,fill=ctk.BOTH, expand=True)

    y=ctk.CTkEntry(frame,fg_color="#817A90",placeholder_text="Name",placeholder_text_color="#FFEAEC",text_color="#FFEAEC",font=("nexa bold", 20),border_width=0)
    y.pack(side=ctk.LEFT,pady=10, padx=10,fill=ctk.BOTH, expand=True)

    z = ctk.CTkCheckBox(frame,fg_color="#817A90", text="Run!",font=("nexa bold",20),text_color="#FFEAEC",border_color="#817A90",checkbox_height=30,
                        checkbox_width=30,border_width=4,hover_color="#817A90",onvalue=1,offvalue=0)

    z.pack(padx=(10,0), pady=10)

    print(trigger)

    c+=1 # counter +1

    return frame

add = ctk.CTkButton(root, fg_color="#3C3744", text="add",font=("nexa bold",20),text_color="#FFEAEC",command=add)
add.pack(side=ctk.LEFT, padx=(20,10), pady=(10,30), fill=ctk.BOTH, expand=True)

delete = ctk.CTkButton(root, fg_color="#3C3744", text="delete",font=("nexa bold",20),text_color="#FFEAEC")
delete.pack(side=ctk.LEFT, padx=(10,20), pady=(10,30), fill=ctk.BOTH, expand=True)

root.mainloop()