import PIL.ImageTk
import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ctypes

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = tk.Tk()
root.title("DYLAN !!!!")
root.iconbitmap("bird_black.ico")
root.config(bg="#242424")
root.geometry("1280x960")

barTop = tk.Frame(root, bg="#3C3744", height=50)
barTop.pack(side="top", fill=tk.X)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

menuState = True
toggleState = "ON"

menuOpenImage = PhotoImage(file="menuOpen.png")
menuCloseImage = PhotoImage(file="menuClose.png")

def switch():
    global menuState
    if menuState is True:
        for b in range(60):
            menuFrame.place(x=0, y=b * 3)
            barTop.update()

        barTop.config(bg="#3C3744")
        root.config(bg="#242424")

        menuState = False

    else:
        barTop.config(bg="#3C3744")
        root.config(bg="#242424")

        for b in range(-60, 0):
            menuFrame.place(x=0, y=-b * 3)
            barTop.update()

        menuState = True

def hi():
    print("e")

topBar = tk.Button(barTop, image=menuOpenImage, bg="#3C3744", activebackground="#3C3744", bd=0, padx=20, command=switch)
topBar.place(x=10, y=10)

menuFrame = tk.Frame(root, bg="#3C3744", height=100, width=1200)
menuFrame.place(relx=0.5, rely=0.9, anchor=CENTER)

y = 80
options = ["MENU", "CONFIG", "CHAT", "HELP"]
def button(a,x,y,cmd):

    def invert_colors(event):
        bg = but.cget("bg")
        fg = but.cget("fg")
        but.config(background=fg, foreground=bg)

    but = tk.Button(menuFrame, text=options[a], font=("nexa bold", 30), bg="#3C3744", fg="#817A90", activebackground="#242424", activeforeground="#FFEAEC", bd=0, command=cmd, anchor=tk.CENTER, width=10)
    but.place(rely=0.5, relx=0.5, x=x, y=y, anchor=CENTER)

button(0,-450,0,hi())
button(1,-150,0,hi())
button(2,150,0,hi())
button(3,450,0,hi())


def toggle():
    global toggleState
    if toggleState == "ON":
        togglebutton.config(fg="#f54242", activeforeground="#f54242")
        togglebutton.config(text="OFF")
        toggleState = "OFF"

    else:
        togglebutton.config(fg="#42f584", activeforeground="#42f584")
        togglebutton.config(text="ON")
        toggleState = "ON"

label = ctk.CTkLabel(master=frame, text="DYLAN.AI", text_color="#FFEAEC", font=("Nexa Heavy", 70), anchor=tk.CENTER)
label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-115)

label = ctk.CTkLabel(master=frame, text="Dynamic Yielding Language and Automated Navigation", text_color="#FFEAEC", font=("Nexa Heavy", 15))
label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-65)

togglebutton = tk.Button(text=toggleState, font=("nexa heavy", 90), bg="#242424", fg="#42f584", activebackground="#3C3744", activeforeground="#42f584", bd=0, anchor=tk.CENTER, width=10, command=toggle)
togglebutton.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=200)

root.mainloop()