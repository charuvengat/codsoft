import tkinter as tk
from tkinter import messagebox
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.first_num_label = tk.Label(root, text="First Number")
        self.first_num_label.grid(row=0, column=0)
        self.first_num_entry = tk.Entry(root)
        self.first_num_entry.grid(row=0, column=1)

        self.second_num_label = tk.Label(root, text="Second Number")
        self.second_num_label.grid(row=1, column=0)
        self.second_num_entry = tk.Entry(root)
        self.second_num_entry.grid(row=1, column=1)

        self.operation_label = tk.Label(root, text="Operation")
        self.operation_label.grid(row=2, column=0)
        self.operation_var = tk.StringVar(root)
        self.operation_var.set("Add")
        self.operation_menu = tk.OptionMenu(root, self.operation_var, "Add", "Subtract", "Multiply", "Divide")
        self.operation_menu.grid(row=2, column=1)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate(self):
        try:
            num1 = float(self.first_num_entry.get())
            num2 = float(self.second_num_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers.")
            return

        operation = self.operation_var.get()
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        self.result_label.config(text=f"Result: {result}")
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
