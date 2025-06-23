#A simple Python Tkinter GUI program implementing a student login form with username and password validation.
import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "student" and password == "password":
        messagebox.showinfo("Login Success", "Welcome, student!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Student Login")

label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

root.mainloop()
