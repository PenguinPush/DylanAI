import customtkinter as ctk
import tkinter as tk
import customtkinter 
from tkinter import *
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#MENU START
menuSwitch = False

root = ctk.CTk()
root.geometry("800x500")
root.title("Dylan.Ai")

color = {"orange": "#FF8700"}

menuOpen = PhotoImage(file="menuOpen.png")
menuClose = PhotoImage(file="menuClose.png")

barTop = tk.Frame(root, bg=color["orange"], height=50)
barTop.pack(side="top", fill=tk.X)

menuOpenButton = tk.Button(barTop, image=menuOpen,bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=None)
menuOpenButton.place(x=10, y=10)

menuBar = tk.Frame(root, bg="gray17", height=1000, width=300)
menuBar.place(x=-300,y=0)
tk.Label(menuBar, font="bahnschriftLight 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

y = 80

options = ["Menu", "Macros", "Help"]

for i in range(3):
    tk.Button(menuBar, text=options[i], font="bahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground = "gray17", activeforeground="green", bd=0).place(x=25,y=y)
    y +=40
    
menuCloseButton = tk.Button(menuBar, image=menuClose, bg=color["orange"], activebackground=color["orange"], bd=0, command=None)





#MENU CLOSE


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="DYLAN.AI", text_color="#FFEAEC", font=("nexa bold", 70))
label.pack(pady=12, padx=10)


root.mainloop()
