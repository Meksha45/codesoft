import sqlite3 as sql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# -------------------- Functions --------------------
def add_task():
    task = task_field.get().strip()
    if not task:
        messagebox.showinfo('Input Error', 'Please enter a task before adding.')
        return
    tasks.append(task)
    the_cursor.execute('INSERT INTO tasks VALUES (?)', (task,))
    update_list()
    task_field.delete(0, 'end')

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
            update_list()
    except:
        messagebox.showinfo('Selection Error', 'Please select a task to remove.')

def delete_all_tasks():
    if messagebox.askyesno('Delete All', 'Are you sure you want to delete all your tasks?'):
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        update_list()

def update_list():
    task_listbox.delete(0, 'end')
    for task in tasks:
        task_listbox.insert('end', task)

def load_tasks_from_db():
    tasks.clear()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

def close_app():
    the_connection.commit()
    the_cursor.close()
    root.destroy()

# -------------------- GUI --------------------
root = tk.Tk()
root.title("✨ Stylish To-Do List App")
root.geometry("700x450+500+250")
root.resizable(False, False)
root.configure(bg="#EAF6F6")

# Database setup
the_connection = sql.connect('listOfTasks.db')
the_cursor = the_connection.cursor()
the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')
tasks = []

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=6)
style.map("TButton",
          foreground=[('pressed', 'white'), ('active', 'black')],
          background=[('pressed', '#117864'), ('active', '#ABEBC6')])

# Header
header = tk.Frame(root, bg="#76D7C4", height=60)
header.pack(fill="x")

header_label = tk.Label(
    header, text="📋  My To-Do List", font=("Segoe UI", 20, "bold"),
    bg="#76D7C4", fg="white"
)
header_label.pack(pady=10)

# Main content
main_frame = tk.Frame(root, bg="#EAF6F6")
main_frame.pack(pady=20)

# Task entry
task_label = tk.Label(
    main_frame, text="Enter a new task:", font=("Segoe UI", 14),
    bg="#EAF6F6", fg="#2E4053"
)
task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

task_field = tk.Entry(main_frame, font=("Segoe UI", 14), width=40, bg="white", fg="black")
task_field.grid(row=0, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(main_frame, bg="#EAF6F6")
button_frame.grid(row=1, column=0, columnspan=2, pady=15)

add_btn = ttk.Button(button_frame, text="➕ Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = ttk.Button(button_frame, text="🗑 Remove Task", command=delete_task)
delete_btn.grid(row=0, column=1, padx=10)

delete_all_btn = ttk.Button(button_frame, text="🚫 Delete All", command=delete_all_tasks)
delete_all_btn.grid(row=0, column=2, padx=10)

exit_btn = ttk.Button(main_frame, text="❌ Exit / Close", command=close_app)
exit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Task list
task_listbox = tk.Listbox(
    main_frame, width=65, height=10, font=("Segoe UI", 12),
    bg="white", fg="black", selectbackground="#58D68D", selectforeground="black"
)
task_listbox.grid(row=2, column=0, columnspan=2, pady=10)

# Load existing tasks
load_tasks_from_db()
update_list()

# Start the application
root.mainloop()
