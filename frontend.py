import tkinter as tk
import customtkinter 
from tkinter import *
from tkinter import ttk

color = {"orange": "#FF8700"}

# sidebar

root = tk.Tk()
root.title("Dylan")
root.geometry("750x450")

State = False

MenuOpen = PhotoImage(file="menuOpen.png")
MenuClose = PhotoImage(file="menuClose.png")

topBar = tk.Frame(root, bg=color["orange"])
topBar.pack(side="top", fill=tk.X)


root.mainloop()

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")


def login():
    print("Test")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="POLAR", text_color="#FFEAEC", font=("nexa bold", 30))
label.pack(pady=12, padx=10)

button1 = ctk.CTkLabel(master=frame, text="Login")
button1.pack(pady=12, padx=10)

button2 = ctk.CTkLabel(master=frame, text="Login2")
button2.pack(pady=12, padx=10)

button1.grid(padx=10, pady=10)
button2.grid(padx=10, pady=10)

checkbox = ctk.CTkCheckBox(master=frame, text="nas")
checkbox.pack(pady=12, padx=10)

root.mainloop()
