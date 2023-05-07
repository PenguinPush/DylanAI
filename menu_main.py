import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = tk.Tk()
root.title("DYLAN.AI")
root.iconbitmap("bird_black.ico")
root.config(bg="#242424")
root.geometry("1280x960")


class MainMenu():
    global label_text
    label_text = ""
    def __init__(self):

        barTop = tk.Frame(root, bg="#3C3744", height=0)
        barTop.pack(side="top", fill=tk.X)

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        bird_image = Image.open("bird_white.png")
        bird_image = bird_image.resize((100, 100), Image.ANTIALIAS)
        bird_image_tk = ImageTk.PhotoImage(bird_image)

        bird_label = tk.Label(image=bird_image_tk)
        bird_label.image = bird_image_tk

        bird_label.place(relx=0.5, rely=0.4, anchor=CENTER, x=365, y=-105, width=100, height=100)

        label = ctk.CTkLabel(master=frame, text="DYLAN.AI ", text_color="#FFEAEC", font=("Nexa Heavy", 140), anchor=tk.CENTER)
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-110)

        label = ctk.CTkLabel(master=frame, text="Dynamic Yielding Language-based Assistant and Navigator", text_color="#817A90", font=("Nexa Heavy", 15))
        label.place(relx=0.5, rely=0.4, anchor=CENTER, y=-32.5)

        self.infolabels = []

        for i in range(3):
            infolabel = ctk.CTkLabel(master=frame, text=label_text, text_color="#FFEAEC", font=("Nexa Heavy", 30))
            infolabel.place(relx=0.5, rely=0.5, anchor=CENTER, y=i * 50)
            self.infolabels.append(infolabel)

    def update_label_text(self, text):
        self.label_text = text
        for infolabel in self.infolabels:
            infolabel.config(text=self.label_text)


MainMenu()
root.mainloop()
