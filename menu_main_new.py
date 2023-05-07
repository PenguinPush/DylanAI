import tkinter as tk
import customtkinter as ctk
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

LARGE_FONT = ("Verdana", 12)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class MenuManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("DYLAN.AI")
        self.iconbitmap("bird_black.ico")
        self.config(bg="#242424")
        self.geometry("1280x960")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global toggleState
        toggleState = "ON"

        barTop = tk.Frame(controller, bg="#3C3744", height=0)
        barTop.pack(side="top", fill=tk.X)

        frame = ctk.CTkFrame(master=controller)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        toggleState = "ON"

        def hi():
            print("e")

        menuFrame = tk.Frame(controller, bg="#3C3744", height=100, width=1200)
        menuFrame.place(relx=0.5, rely=0.9, anchor=CENTER)

        y = 80
        options = ["MENU", "CONFIG", "HELP"]

        def button(a, x, y, cmd):
            but = tk.Button(menuFrame, text=options[a], font=("nexa bold", 30), bg="#3C3744", fg="#817A90",
                            activebackground="#242424", activeforeground="#FFEAEC", bd=0, command=cmd, anchor=tk.CENTER,
                            width=10)
            but.place(rely=0.5, relx=0.5, x=x, y=y, anchor=CENTER)

        button(0, -300, 0, hi())
        button(1, 0, 0, hi())
        button(2, 300, 0, hi())

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

        bird_image = Image.open("bird_white.png")
        bird_image = bird_image.resize((100, 100), Image.ANTIALIAS)
        bird_image_tk = ImageTk.PhotoImage(bird_image)

        bird_label = tk.Label(image=bird_image_tk)
        bird_label.image = bird_image_tk

        bird_label.place(relx=0.5, rely=0.4, anchor=CENTER, x=365, y=-105, width=100, height=100)

        label = ctk.CTkLabel(master=frame, text="DYLAN.AI ", text_color="#FFEAEC", font=("Nexa Heavy", 140),
                             anchor=tk.CENTER)
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-110)

        label = ctk.CTkLabel(master=frame, text="Dynamic Yielding Language and Automated Navigation",
                             text_color="#817A90", font=("Nexa Heavy", 15))
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-32.5)

        togglebutton = tk.Button(text=toggleState, font=("nexa heavy", 90), bg="#242424", fg="#42f584",
                                 activebackground="#3C3744", activeforeground="#42f584", bd=0, anchor=tk.CENTER,
                                 width=10, command=toggle)
        togglebutton.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=200)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = MenuManager()
app.mainloop()