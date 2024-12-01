import tkinter as tk
from tkinter import messagebox, simpledialog
import json

def add_task():
    task = task_entry.get()
    if task:
        task_ListBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_ListBox.curselection()
    if selected_task:
        task_ListBox.delete(selected_task)

def mark_task():
    selected_task = task_ListBox.curselection()
    if selected_task:
        task_ListBox.itemconfig(selected_task, bg="chocolate3")

def edit_task():
    selected_task = task_ListBox.curselection()
    if selected_task:
        current_task = task_ListBox.get(selected_task)
        new_task = simpledialog.askstring("Редактировать задачу", "Изменить задачу", initialvalue=current_task)
        if new_task:
            task_ListBox.delete(selected_task)
            task_ListBox.insert(selected_task, new_task)

def sort_tasks():
    tasks = list(task_ListBox.get(0, tk.END))
    tasks.sort()
    task_ListBox.delete(0, tk.END)
    for task in tasks:
        task_ListBox.insert(tk.END, task)

def save_tasks():
    tasks = task_ListBox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    messagebox.showinfo("Информация", "Задачи сохранены!")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            task_ListBox.delete(0, tk.END)
            for task in tasks:
                task_ListBox.insert(tk.END, task)
        messagebox.showinfo("Информация", "Задачи загружены!")
    except FileNotFoundError:
        messagebox.showwarning("Ошибка", "Файл с задачами не найден!")


root = tk.Tk()
root.title("Task title")
root.configure(bg="aquamarine4")

text1 = tk.Label(root, text="Введите ваш текст", bg="aquamarine4")
text1.pack(pady=5)

task_entry = tk.Entry(root,width=30, bg="azure1")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

edit_button = tk.Button(root, text="Редактировать задачу", command=edit_task)
edit_button.pack(pady=5)

sort_button = tk.Button(root, text="Сортировать задачи", command=sort_tasks)
sort_button.pack(pady=5)

save_button = tk.Button(root, text="Сохранить задачи", command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Загрузить задачи", command=load_tasks)
load_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач", bg="aquamarine4")
text2.pack(pady=5)

task_ListBox = tk.Listbox(root, height=10, width=50, bg="aquamarine3")
task_ListBox.pack(pady=5)

root.mainloop()