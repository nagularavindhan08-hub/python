import tkinter as tk
from tkinter import messagebox
import math

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

def square():
    try:
        num = float(entry.get())
        result = num ** 2
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Enter a valid number")

def square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Enter a valid number")

# Window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x500")
root.configure(bg="#2C3E50")
root.resizable(False, False)

# Display
entry = tk.Entry(
    root,
    font=("Arial", 22),
    bd=8,
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Buttons
buttons = [
    ['C', '⌫', '√', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', 'x²', '=']
]

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame, bg="#2C3E50")
    row_frame.pack(expand=True, fill="both")

    for btn in row:

        if btn == "=":
            command = calculate
        elif btn == "C":
            command = clear
        elif btn == "⌫":
            command = backspace
        elif btn == "√":
            command = square_root
        elif btn == "x²":
            command = square
        else:
            command = lambda b=btn: click(b)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 16, "bold"),
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            command=command
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Keyboard Support
def key_press(event):
    key = event.char

    if key in "0123456789+-*/.":
        click(key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()

root.bind("<Key>", key_press)

root.mainloop()
