import customtkinter as ctk
import tkinter as tk
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = tk.Tk()
root.title("DYLAN.AI")
root.iconbitmap("bird_black.ico")
root.config(bg="#242424")
root.geometry("1280x960")

class MainMenu():
    def __init__(self):

        global toggleState
        toggleState = "ON"

        barTop = tk.Frame(root, bg="#3C3744", height=0)
        barTop.pack(side="top", fill=tk.X)

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        menuState = True
        toggleState = "ON"

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
        def button(a, x , y, cmd):

            def invert_colors(event):
                bg = but.cget("bg")
                fg = but.cget("fg")
                but.config(background=fg, foreground=bg)

            but = tk.Button(menuFrame, text=options[a], font=("nexa bold", 30), bg="#3C3744", fg="#817A90", activebackground="#242424", activeforeground="#FFEAEC", bd=0, command=cmd, anchor=tk.CENTER, width=10)
            but.place(rely=0.5, relx=0.5, x=x, y=y, anchor=CENTER)

        button(0,-300,0,hi())
        button(1,0,0,ConfigMenu)
        button(2,300,0,hi())

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

        label = ctk.CTkLabel(master=frame, text="DYLAN.AI ", text_color="#FFEAEC", font=("Nexa Heavy", 140), anchor=tk.CENTER)
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-110)

        label = ctk.CTkLabel(master=frame, text="Dynamic Yielding Language and Automated Navigation", text_color="#817A90", font=("Nexa Heavy", 15))
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-32.5)

        togglebutton = tk.Button(text=toggleState, font=("nexa heavy", 90), bg="#242424", fg="#42f584", activebackground="#3C3744", activeforeground="#42f584", bd=0, anchor=tk.CENTER, width=10, command=toggle)
        togglebutton.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=200)

class ConfigMenu():
    def __init__(self):
        filename = " "
        trigger = []
        c = 0  # amount of inputs given
        dataBase = open('custom_macros.txt', 'w')
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="MACRO LIST:", text_color="#FFEAEC", font=("nexa bold", 30))
        label.pack(pady=(40, 20), padx=30)

        scroll = ctk.CTkScrollableFrame(master=frame, corner_radius=20, fg_color="#3C3744", width=600, height=300,
                                        scrollbar_button_color="#817A90", scrollbar_button_hover_color="#FFEAEC")
        scroll.pack(pady=20, padx=0)

        def add():
            global c, filename

            def browseFiles():
                global filename
                filename = filedialog.askopenfilename(initialdir="/",
                                                      title="SELECT A FILE",
                                                      filetypes=(("all files", "*.*"), ("txt files", "*.txt")))
                x.configure(text=os.path.basename(filename))
                filename = " "
                return filename

            frame = ctk.CTkFrame(scroll, fg_color="#3C3744")
            frame.pack(pady=5, fill=ctk.X, expand=True)
            x = ctk.CTkButton(frame, fg_color="#817A90", text=filename, text_color="#FFEAEC", font=("nexa bold", 20),
                              border_width=0, state="readonly", command=browseFiles, anchor="w")
            x.pack(side=ctk.LEFT, pady=10, padx=20, fill=ctk.BOTH, expand=True)
            y = ctk.CTkEntry(frame, fg_color="#817A90", placeholder_text="Name", placeholder_text_color="#FFEAEC",
                             text_color="#FFEAEC", font=("nexa bold", 20), border_width=0)
            y.pack(side=ctk.LEFT, pady=10, padx=10, fill=ctk.BOTH, expand=True)
            z = ctk.CTkCheckBox(frame, fg_color="#817A90", text="Run!", font=("nexa bold", 20), text_color="#FFEAEC",
                                border_color="#817A90", checkbox_height=30,
                                checkbox_width=30, border_width=4, hover_color="#817A90", onvalue=1, offvalue=0)
            z.pack(padx=(10, 0), pady=10)
            c += 1  # counter +1
            trigger.append(frame)
            dataBase.write('\n' + str(frame))

        def delete():
            global trigger
            frame = trigger[len(trigger) - 1]
            frame.destroy()
            trigger = trigger[:len(trigger) - 1]

        new = ctk.CTkButton(root, fg_color="#3C3744", text="add", font=("nexa bold", 20), text_color="#FFEAEC", command=add)
        new.pack(side=ctk.LEFT, padx=(40, 20), pady=(10, 30), fill=ctk.BOTH, expand=True)

        delete = ctk.CTkButton(root, fg_color="#3C3744", text="delete", font=("nexa bold", 20), text_color="#FFEAEC",
                               command=delete)
        delete.pack(side=ctk.LEFT, padx=(20, 40), pady=(10, 30), fill=ctk.BOTH, expand=True)

MainMenu()
root.mainloop()