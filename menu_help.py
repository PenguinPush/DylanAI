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
root.title("DYLAN.AI")
root.iconbitmap("bird_black.ico")
root.config(bg="#242424")
root.geometry("720x720")

barTop = tk.Frame(root, bg="#3C3744", height=0)
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

menuFrame = tk.Frame(root, bg="#3C3744", height=100, width=1200)
menuFrame.place(relx=0.5, rely=0.9, anchor=CENTER)

y = 80
options = ["MENU", "CONFIG", "HELP"]
def button(a,x,y,cmd):

    def invert_colors(event):
        bg = but.cget("bg")
        fg = but.cget("fg")
        but.config(background=fg, foreground=bg)

    but = tk.Button(menuFrame, text=options[a], font=("nexa bold", 30), bg="#3C3744", fg="#817A90", activebackground="#242424", activeforeground="#FFEAEC", bd=0, command=cmd, anchor=tk.CENTER, width=10)
    but.place(rely=0.5, relx=0.5, x=x, y=y, anchor=CENTER)

button(0,-300,0,hi())
button(1,0,0,hi())
button(2,300,0,hi())

#END


label = ctk.CTkLabel(master=frame, text="HELP", text_color="#FFEAEC", font=("Nexa Heavy", 100), anchor=tk.CENTER)
label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-210)

label = ctk.CTkLabel(master=frame, text="How do you use DYLAN.AI? ", text_color="#817A90", font=("Nexa Heavy", 20))
label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-150)

scroll = ctk.CTkScrollableFrame(label_text="""
                                What is DYLAN.AI?
                                
                                Dylan.AI,Dynamic Yielding Language and Automated Navigation - Artificial Intelligence, is an AI-Driven tool to perform certain actions that would be impossible normally.
                                It takes input through voice commands in the mic, parses it into a command for the computer, and executes the command. 


                                """, master=frame,corner_radius=20, fg_color="#3C3744", width=300, height=5,scrollbar_button_color="#817A90",scrollbar_button_hover_color="#FFEAEC")
                                
                                


scroll.place(relx=0.5, rely=0.5, anchor=CENTER, y=50)



root.mainloop()