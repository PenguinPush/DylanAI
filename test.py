import ctk

def validate_text(entry):
    text = entry.get()
    if len(text) > 10:
        # If text is longer than 10 characters, truncate it to 10 characters
        entry.set(text[:10])
    return True

# Create a CTKENTRY widget and add the validation function
entry = ctk.CTKENTRY()
entry.add_validator(validate_text)