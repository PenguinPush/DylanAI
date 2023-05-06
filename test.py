import customtkinter as ctk

# Create the main window
root = ctk.CTk()

# Create a label widget
label1 = ctk.CTkLabel(root, text="Label 1")
label1.pack()

# Create a second label widget and place it below the first label
label2 = ctk.CTkLabel(root, text="Label 2")
label2.place(relx=0, rely=0, x=0, y=label1.winfo_height()+10)

# Start the main event loop
root.mainloop()