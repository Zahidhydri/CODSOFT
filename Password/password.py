import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        password = generate_password(password_length)
        result_label.config(text="Generated Password: " + password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
