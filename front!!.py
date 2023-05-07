import customtkinter as ctk
import tkinter as ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

color = {"white": "#FFEAEC"}
color = {"blackk": "#3C3744"}

root = ctk.CTk()
root.geometry("800x500")

def login():
    print("Test")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="POLAR", text_color="#FFEAEC", font=("nexa bold", 30))
label.pack(pady=50, padx=50)

Macros = ctk.CTkButton(master=frame, fg_color="#3C3744", text="Macros")
Macros.pack(side=ctk.LEFT, padx=20, pady=0, fill=ctk.BOTH, expand=True)

Help = ctk.CTkButton(master=frame, fg_color="#3C3744", text="Help")
Help.pack(padx=20, pady=0) 

root.mainloop()
