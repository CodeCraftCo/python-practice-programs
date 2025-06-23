#A simple Python Tkinter program demonstrating how to create and display a label widget in a GUI window.
import tkinter as tk

root = tk.Tk()  # Create the main window
root.title("Label Widget")

label_username = tk.Label(root, text="Welcome to PDVVP Polytechnic College")
label_username.pack()  # Display the label

root.geometry("500x400")  # Set window size
root.mainloop()  # Start the main event loop