import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

root.mainloop()
