import tkinter as tk
import random
import string


def generate_password():
    length = length_scale.get()
    includeUppercase = uppercase_var.get()
    includeNumbers = numbers_var.get()
    includeSymbols = symbols_var.get()

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if includeUppercase else ''
    number = string.digits if includeNumbers else ''
    symbol = string.punctuation if includeSymbols else ''

    all_chars = lowercase + uppercase + number + symbol

    password = ''.join(random.choices(all_chars, k=length))

    password_label.config(text=password)


root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Length:")
length_scale = tk.Scale(root, from_=8, to=64, orient=tk.HORIZONTAL)
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
generate_button = tk.Button(root, text="Generate password", command=generate_password)
password_label = tk.Label(root, text="")

length_scale.set(8)
uppercase_var.set(False)
numbers_var.set(False)
symbols_var.set(False)

length_label.grid(row=0, column=0)
length_scale.grid(row=0, column=1)
uppercase_check.grid(row=1, column=0, columnspan=2)
numbers_check.grid(row=2, column=0, columnspan=2)
symbols_check.grid(row=3, column=0, columnspan=2)
generate_button.grid(row=4, column=0, columnspan=2)
password_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
