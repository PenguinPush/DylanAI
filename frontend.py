import customtkinter as ctk

# Create the main window
root = ctk.CTk()


# Create a list of options for the combo box
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Create a combo box widget
combo_box = ctk.CTkComboBox(root, values=options)

# Set the default option to the first option in the list
combo_box.set(options[0])

# Define a function to update the label with the selected option
def update_label(selection):
    label.config(text="Selected option: " + selection)

# Bind the update_label function to the combo box
combo_box.bind("<<ComboboxSelected>>", lambda event: update_label(combo_box.get()))

# Use grid layout manager to place the combo box widget
combo_box.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()