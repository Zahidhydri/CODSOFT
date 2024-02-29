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
zahid = tk.Tk()
zahid.title("Password Generator")
zahid.configure(background='#91f',relief="ridge",bd=10)
zahid.resizable(0,0)

# Create and pack widgets
length_label = tk.Label(zahid,font = ('cooper black',26,'bold'), text="Zahid .S. Hydri",bg="#91f",fg="#fff")
length_label.pack(pady=5)
length_label = tk.Label(zahid,font = ('cooper black',32,'bold'), text="Enter Password Length:",bg="#91f")
length_label.pack(pady=5)

length_entry = tk.Entry(zahid,font = ('arial',24,'bold'),bd=10,bg="#99f")
length_entry.pack(pady=5)

generate_button = tk.Button(zahid,font = ('bausaus',20,'bold'),bg="#9f1",bd=10, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

result_label = tk.Label(zahid,font = ('cooper black',32,'bold'), text="",bg="#91f")
result_label.pack(pady=10)

# Start the Tkinter event loop
zahid.mainloop()
