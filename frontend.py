
import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# MENU START
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

root = tk.Tk()
root.title("DYLAN !!!!")
root.config(bg="#242424")
root.geometry("800x600")

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
        for x in range(301):
            menuFrame.place(x=-x, y=0)
            barTop.update()

       
        barTop.config(bg="#3C3744")
        root.config(bg="#242424")

        menuState = False
    else:
       
        barTop.config(bg="#3C3744")
        root.config(bg="#242424")

        for x in range(-300, 0):
            menuFrame.place(x=x, y=0)
            barTop.update()

        menuState = True





topBar = tk.Button(barTop, image=menuOpenImage, bg="#3C3744", activebackground="#3C3744", bd=0, padx=20, command=switch)
topBar.place(x=10, y=10)

label = ctk.CTkLabel(master=frame, text="DYLAN.AI", text_color="#FFEAEC", font=("nexa bold", 70))
label.pack(pady=12, padx=10)

menuFrame = tk.Frame(root, bg="#242424", height=1000, width=300)
menuFrame.place(x=-300, y=0)
tk.Label(menuFrame, font="Bahnschrift 15", bg="#817A90", fg="#3C3744", height=2, width=300, padx=20).place(x=0, y=-4)

y = 80
options = ["Menu", "Dylan", "Help"]
for i in range(3):
    tk.Button(menuFrame, text=options[i], font=("nexa bold", 30), bg="#3C3744", fg="#817A90", activebackground="#3C3744", activeforeground="#FFEAEC", bd=0).place(x=25, y=y)
    y += 110

menuClose = tk.Button(menuFrame, image=menuCloseImage, bg="#817A90", bd=0, command=switch)
menuClose.place(x=250, y=10)

root.mainloop()


# MENU CLOSE



root.mainloop()