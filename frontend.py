import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")

def login():
    print("Test")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="POLAR", text_color="#FFEAEC", font=("nexa bold", 30))
label.pack(pady=12, padx=10)

button1 = ctk.CTkLabel(master=frame, text="Login")
button1.pack(pady=12, padx=10)

button2 = ctk.CTkLabel(master=frame, text="Login2")
button2.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="nas")
checkbox.pack(pady=12, padx=10)

root.mainloop()
