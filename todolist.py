#GUI version
import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title} - {self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(self, index, title, description):
        self.tasks[index].title = title
        self.tasks[index].description = description

    def delete_task(self, index):
        del self.tasks[index]

    def mark_task_completed(self, index):
        self.tasks[index].mark_as_completed()

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo_list = ToDoList()

        self.title_var = tk.StringVar()
        self.desc_var = tk.StringVar()

        tk.Label(root, text="Task Title").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.title_var).grid(row=0, column=1)
        tk.Label(root, text="Task Description").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.desc_var).grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=3, column=0, columnspan=2)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=4, column=0)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=4, column=1)
        self.mark_completed_button = tk.Button(root, text="Mark Completed", command=self.mark_task_completed)
        self.mark_completed_button.grid(row=5, column=0, columnspan=2)

    def add_task(self):
        title = self.title_var.get()
        description = self.desc_var.get()
        self.todo_list.add_task(title, description)
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.view_tasks():
            self.task_listbox.insert(tk.END, str(task))

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            title = self.title_var.get()
            description = self.desc_var.get()
            self.todo_list.update_task(index, title, description)
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.delete_task(index)
            self.update_task_listbox()

    def mark_task_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.mark_task_completed(index)
            self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


