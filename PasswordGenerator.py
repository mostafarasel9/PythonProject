import random
import string
from tkinter import *
def generate_password():
    try:
        length = int(length_input.get())  # Get the desired password length
    except ValueError:
        result_display.delete(0, END)
        result_display.insert(0, "Invalid length!")  # Show error if length is not a number
        return

    include_uppercase = uppercase_var.get()  # Check if uppercase is selected
    include_lowercase = lowercase_var.get()  # Check if lowercase is selected
    include_numbers = numbers_var.get()  # Check if numbers are selected
    include_symbols = symbols_var.get()  # Check if symbols are selected

    # Build the character pool based on selected options
    char_pool = ''
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation

    # Ensure at least one character type is selected
    if not char_pool:
        result_display.delete(0, END)
        result_display.insert(0, "Select at least one option!")  # Show error if no options are selected
        return

    # Generate the password by randomly picking characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    # Display the generated password
    result_display.delete(0, END)  # Clear the previous result
    result_display.insert(0, password)  # Insert the new password
# Initialize the GUI window
root = Tk()
root.title("Password Generator")
root.geometry("400x300")

# Input: Password length
Label(root, text="Password Length:", font=("Helvetica", 10)).pack(pady=5)
length_input = Entry(root, width=10)
length_input.pack(pady=5)

# Options: Character types
uppercase_var = BooleanVar(value=True)
lowercase_var = BooleanVar(value=True)
numbers_var = BooleanVar(value=True)
symbols_var = BooleanVar(value=True)

Label(root, text="Include:", font=("Helvetica", 10)).pack(pady=5)
Checkbutton(root, text="Uppercase Letters", variable=uppercase_var).pack(anchor=W)
Checkbutton(root, text="Lowercase Letters", variable=lowercase_var).pack(anchor=W)
Checkbutton(root, text="Numbers", variable=numbers_var).pack(anchor=W)
Checkbutton(root, text="Symbols", variable=symbols_var).pack(anchor=W)

# Generate button
Button(root, text="Generate Password", command=generate_password, bg="lightblue").pack(pady=10)

# Output display (copyable)
Label(root, text="Generated Password:", font=("Helvetica", 10)).pack(pady=5)
result_display = Entry(root, font=("Helvetica", 12), fg="green", width=40)
result_display.pack(pady=5)

# Run the application
root.mainloop()