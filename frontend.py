
import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# MENU START
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

root = tk.Tk()
root.title("Tkinter Navbar")
root.config(bg="gray17")
root.geometry("800x500")

menuState = False

menuOpenImage = PhotoImage(file="menuOpen.png")
menuCloseImage = PhotoImage(file="menuClose.png")

def switch():
    global menuState
    if menuState is True:
        for x in range(301):
            menuFrame.place(x=-x, y=0)
            barTop.update()

       
        barTop.config(bg=color["orange"])
        root.config(bg="gray17")

        menuState = False
    else:
       
        barTop.config(bg=color["nero"])
        root.config(bg=color["nero"])

        for x in range(-300, 0):
            menuFrame.place(x=x, y=0)
            barTop.update()

        menuState = True

barTop = tk.Frame(root, bg=color["orange"], height=50)
barTop.pack(side="top", fill=tk.X)



topBar = tk.Button(barTop, image=menuOpenImage, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
topBar.place(x=10, y=10)

menuFrame = tk.Frame(root, bg="gray17", height=1000, width=300)
menuFrame.place(x=-300, y=0)
tk.Label(menuFrame, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

y = 80
options = ["Menu", "Dylan", "Help"]
for i in range(3):
    tk.Button(menuFrame, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

menuClose = tk.Button(menuFrame, image=menuCloseImage, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
menuClose.place(x=250, y=10)

root.mainloop()


# MENU CLOSE

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="DYLAN.AI", text_color="#FFEAEC", font=("nexa bold", 70))
label.pack(pady=12, padx=10)

root.mainloop()