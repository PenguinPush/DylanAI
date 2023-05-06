import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

color = {"white": "#FFEAEC"}

root = ctk.CTk()
root.title("i want to fucking die")
root.geometry("800x600")

def login():
    print("Test")

c=0
macros = []

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Macro list:", text_color="#FFEAEC", font=("nexa bold", 30))
label.pack(pady=(40,20), padx=30)

scroll = ctk.CTkScrollableFrame(master=frame,corner_radius=20, fg_color="#3C3744", width=600, height=300,scrollbar_button_color="#817A90",scrollbar_button_hover_color="#FFEAEC")
scroll.pack(pady=(20,0), padx=0)

def add():
    global c
    x=ctk.CTkEntry(scroll,fg_color="#817A90",placeholder_text="Description",placeholder_text_color="#FFEAEC",font=("nexa bold", 20),border_width=0)
    x.pack(side=ctk.RIGHT,pady=10, padx=(10,20),fill=ctk.BOTH, expand=True)

    y=ctk.CTkEntry(scroll,fg_color="#817A90",placeholder_text="Name",placeholder_text_color="#FFEAEC",font=("nexa bold", 20),border_width=0)
    y.pack(pady=10, padx=10,fill=ctk.X, expand=True)

    options = ["macro","website","open"]
    z = ctk.CTkComboBox(scroll, values=options,fg_color="#817A90",dropdown_text_color="#FFEAEC",font=("nexa bold", 20),
                            dropdown_fg_color="#817A90",border_width=0,text_color="#FFEAEC",dropdown_font=("nexa light", 20),
                            button_color="#817A90",dropdown_hover_color="#3C3744",border_color="#817A90",state="readonly")
    z.set(options[0])
    z.bind("<<ComboboxSelected>>")
    z.pack(padx=10, pady=10)
    #a = ctk.CTkLabel(scroll, text=" ", text_color="#FFFFFF")
    #a.pack(side,padx=10, pady=10, fill=ctk.BOTH, expand=True)

    macros.append({"name": y, "description": x})
    c += 1

add_button = ctk.CTkButton(root, fg_color="#3C3744", text="add",font=("nexa bold",20),text_color="#FFEAEC", command=add)
add_button.pack(side=ctk.LEFT, padx=200, pady=(10,30), fill=ctk.BOTH, expand=True)

root.mainloop()