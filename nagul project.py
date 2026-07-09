import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            department TEXT,
            marks REAL
        )
    """)

    conn.commit()
    conn.close()


# ---------- FUNCTIONS ----------
def add_student():
    name = name_entry.get()
    dept = dept_combo.get()
    marks = marks_entry.get()

    if name == "" or dept == "" or marks == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number.")
        return

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, department, marks) VALUES (?, ?, ?)",
        (name, dept, marks)
    )

    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
    dept_combo.current(0)

    load_students()


def load_students():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

    conn.close()


def delete_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first.")
        return

    student_id = tree.item(selected)["values"][0]

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()

    load_students()


# ---------- MAIN WINDOW ----------
init_db()

root = tk.Tk()
root.title("Student Record Management System")
root.geometry("650x450")

# ---------- INPUT FRAME ----------
frame = ttk.LabelFrame(root, text="Student Details", padding=10)
frame.pack(fill="x", padx=15, pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Department").grid(row=0, column=2, padx=5)

dept_combo = ttk.Combobox(
    frame,
    values=["Computer Science", "Mechanical", "Electrical", "Civil", "Commerce"]
)
dept_combo.grid(row=0, column=3, padx=5)
dept_combo.current(0)

tk.Label(frame, text="Marks").grid(row=1, column=0, padx=5, pady=5)
marks_entry = tk.Entry(frame)
marks_entry.grid(row=1, column=1)

add_btn = tk.Button(
    frame,
    text="Add Student",
    bg="green",
    fg="white",
    command=add_student
)
add_btn.grid(row=1, column=3, padx=5)

# ---------- TABLE ----------
columns = ("ID", "Name", "Department", "Marks")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150)

tree.pack(fill="both", expand=True, padx=15, pady=10)

# ---------- DELETE BUTTON ----------
delete_btn = tk.Button(
    root,
    text="Delete Selected",
    bg="red",
    fg="white",
    command=delete_student
)
delete_btn.pack(pady=10)

load_students()

root.mainloop()