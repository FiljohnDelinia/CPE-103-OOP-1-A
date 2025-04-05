import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.current_input = ""

        self.display = tk.Entry(root, font=("Arial", 24), bd=10, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def create_buttons(self):
        for button_info in self.buttons:
            text, row, col = button_info[:3]
            colspan = button_info[3] if len(button_info) > 3 else 1
            self.create_button(text, row, col, colspan)

    def create_button(self, text, row, col, colspan=1):
        button = tk.Button(self.root, text=text, font=("Arial", 18), height=2, width=5)
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        if text == 'C':
            button.config(command=self.clear_input)
        elif text == '=':
            button.config(command=self.calculate_result)
        else:
            button.config(command=lambda t=text: self.on_button_click(t))

    def on_button_click(self, button_text):
        self.current_input += button_text
        self.update_display()

    def clear_input(self):
        self.current_input = ""
        self.update_display()

    def calculate_result(self):
        try:
            self.current_input = str(eval(self.current_input))
        except Exception:
            self.current_input = "Error"
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_input)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
