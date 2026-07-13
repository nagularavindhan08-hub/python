import tkinter as tk

# Function to display button clicks
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=5, justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Button frame
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            command = calculate
        elif btn == "C":
            command = clear
        else:
            command = lambda b=btn: click(b)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            width=5,
            height=2,
            command=command
        ).pack(side="left", expand=True, fill="both")

root.mainloop()