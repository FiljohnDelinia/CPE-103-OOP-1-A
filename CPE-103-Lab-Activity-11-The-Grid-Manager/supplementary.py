import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)

        self.current_input = ""

        self.display = tk.Entry(root, font=("Arial", 24), bd=10, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sin', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('cos', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('^', 4, 4),
            ('(', 5, 0), (')', 5, 1), ('tan', 5, 2)
        ]

        for i in range(6):
            root.grid_rowconfigure(i, weight=1, uniform="equal")
        for j in range(5):
            root.grid_columnconfigure(j, weight=1, uniform="equal")

        for button_info in buttons:
            text, row, col = button_info
            button = tk.Button(root, text=text, font=("Arial", 18), height=2, width=5)
            if text == "C":
                button.config(command=self.clear_input)
            elif text == "=":
                button.config(command=self.calculate_result)
            elif text in ['sin', 'cos', 'tan']:
                button.config(command=self.create_trig_function_handler(text))
            elif text == "^":
                button.config(command=self.exponentiation)
            else:
                button.config(command=self.create_button_click_handler(text))
            button.grid(row=row, column=col, sticky="nsew")

        root.bind("<Return>", self.calculate_result)

        menubar = tk.Menu(root)
        root.config(menu=menubar)

    def create_button_click_handler(self, text):
        def button_click():
            self.current_input += text
            self.update_display()
        return button_click

    def create_trig_function_handler(self, func):
        def trig_click():
            self.apply_trig_function(func)
        return trig_click

    def apply_trig_function(self, func):
        try:
            angle_in_radians = math.radians(float(self.current_input))
            if func == "sin":
                self.current_input = str(math.sin(angle_in_radians))
            elif func == "cos":
                self.current_input = str(math.cos(angle_in_radians))
            elif func == "tan":
                self.current_input = str(math.tan(angle_in_radians))
            self.update_display()
        except ValueError:
            self.current_input = "Error"
            self.update_display()

    def exponentiation(self):
        self.current_input += "**"
        self.update_display()

    def clear_input(self):
        self.current_input = ""
        self.update_display()

    def calculate_result(self):
        try:
            self.current_input = str(eval(self.current_input))
        except (SyntaxError, ValueError, ZeroDivisionError):
            self.current_input = "Error"
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_input)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
