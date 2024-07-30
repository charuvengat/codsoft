#import the required packages
import tkinter as tk
from tkinter import messagebox
import random
import string

# generate length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#main class
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2)

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(root, state='readonly')
        self.password_entry.grid(row=2, column=1)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
        except ValueError as e:
            messagebox.showerror("Invalid input", f"Please enter a valid number. {e}")
            return

        password = generate_password(length)
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state='readonly')
#run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


