import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# MENU START
menuSwitch = False

root = ctk.CTk()
root.geometry("800x500")
root.title("Dylan.Ai")

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

menuOpen = PhotoImage(file="menuOpen.png")
menuClose = PhotoImage(file="menuClose.png")


def menuSwitchReal():
    global menuSwitch
    if menuSwitch is True:
        for x in range(301):
            menuBar.place(x=-x, y=0)
            root.update()
        brandLabel.config(fg="green")
        homeLabel.config(bg=color["orange"])
        menuSwitch = False
    else:
        brandLabel.config(fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        for x in range(-300, 0):
            menuBar.place(x=x, y=0)
            root.update()
        menuSwitch = True


barTop = tk.Frame(root, bg=color["orange"], height=50)
barTop.pack(side="top", fill=tk.X)

homeLabel = tk.Label(barTop, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="Pythonista\nEmpire", font="System 30", fg="green")
brandLabel.place(x=100, y=250)


menuOpenButton = tk.Button(barTop, image=menuOpen, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=menuSwitchReal)
menuOpenButton.place(x=10, y=10)

menuBar = tk.Frame(root, bg="gray17", height=1000, width=300)
menuBar.place(x=-300, y=0)
tk.Label(menuBar, font="bahnschriftLight 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

y = 80

options = ["Menu", "Macros", "Help"]

for i in range(3):
    tk.Button(menuBar, text=options[i], font="bahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

menuCloseButton = tk.Button(menuBar, image=menuClose, bg=color["orange"], activebackground=color["orange"], bd=0, command=menuSwitchReal)
menuCloseButton.place(x=250, y=10)


# MENU CLOSE

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="DYLAN.AI", text_color="#FFEAEC", font=("nexa bold", 70))
label.pack(pady=12, padx=10)

root.mainloop()