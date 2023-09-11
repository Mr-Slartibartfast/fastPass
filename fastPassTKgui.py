import tkinter as tk
import string
import secrets

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    if length < 1:
        result_label.config(text="Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label for password
password_label = tk.Label(window, text="Generated Password:")
password_label.pack(pady=10)

# Entry to display generated password
password_entry = tk.Entry(window, width=30)
password_entry.pack()

# Label and Entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window, width=10)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display any messages
result_label = tk.Label(window, text="")
result_label.pack()

# Run the GUI
window.mainloop()