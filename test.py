import customtkinter as ctk
import tkinter as tk
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import speech_recognition as sr
from menu_config import main_config
import tempfile
import glob
import multiprocessing
from main import change_output

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = tk.Tk()
root.title("DYLAN.AI")
root.iconbitmap("bird_black.ico")
root.config(bg="#242424")
root.geometry("1280x960")


class MainMenu():
    def __init__(self):

        barTop = tk.Frame(root, bg="#3C3744", height=0)
        barTop.pack(side="top", fill=tk.X)

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # global toggleState
        self.toggleState = "ON"

        def hi():
            print("e")

        def import_menu_config():
            main_config()

        menuFrame = tk.Frame(root, bg="#3C3744", height=100, width=1200)
        menuFrame.place(relx=0.5, rely=0.9, anchor=CENTER)

        y = 80
        options = ["CONFIG"]

        def button(a, x, y, cmd):
            def invert_colors(event):
                bg = but.cget("bg")
                fg = but.cget("fg")
                but.config(background=fg, foreground=bg)

            but = tk.Button(menuFrame, text=options[a], font=("nexa bold", 30), bg="#3C3744", fg="#817A90",
                            activebackground="#242424", activeforeground="#FFEAEC", bd=0, command=cmd, anchor=tk.CENTER,
                            width=40)
            but.place(rely=0.5, relx=0.5, x=x, y=y, anchor=CENTER)

        button(0, 0, 0, import_menu_config)

        # def toggle(self):
        #     # global toggleState
        #     if self.toggleState == "ON":
        #         togglebutton.config(fg="#f54242", activeforeground="#f54242")
        #         togglebutton.config(text="OFF")
        #         self.toggleState = "OFF"
        #         change_output(False)
        #
        #     else:
        #         togglebutton.config(fg="#42f584", activeforeground="#42f584")
        #         togglebutton.config(text="ON")
        #         toggleState = "ON"
        #         change_output(True)

        bird_image = Image.open("bird_white.png")
        bird_image = bird_image.resize((100, 100), Image.ANTIALIAS)
        bird_image_tk = ImageTk.PhotoImage(bird_image)

        bird_label = tk.Label(image=bird_image_tk)
        bird_label.image = bird_image_tk

        bird_label.place(relx=0.5, rely=0.4, anchor=CENTER, x=365, y=-105, width=100, height=100)

        label = ctk.CTkLabel(master=frame, text="DYLAN.AI ", text_color="#FFEAEC", font=("Nexa Heavy", 140),
                             anchor=tk.CENTER)
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-110)

        label = ctk.CTkLabel(master=frame, text="Dynamic Yielding Language-based Assistant and Navigator",
                             text_color="#817A90", font=("Nexa Heavy", 15))
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-32.5)

        self.togglebutton = tk.Button(text=self.toggleState, font=("nexa heavy", 90), bg="#242424", fg="#42f584",
                                 activebackground="#3C3744", activeforeground="#42f584", bd=0, anchor=tk.CENTER,
                                 width=10, command=self.toggle)
        self.togglebutton.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=200)

    def toggle(self):
        # global toggleState
        if self.toggleState == "ON":
            print("off")
            self.togglebutton.config(fg="#f54242", activeforeground="#f54242")
            self.togglebutton.config(text="OFF")
            self.toggleState = "OFF"
            change_output(False)

        else:
            print("on")
            self.togglebutton.config(fg="#42f584", activeforeground="#42f584")
            self.togglebutton.config(text="ON")
            self.toggleState = "ON"
            change_output(True)


MainMenu()
root.mainloop()