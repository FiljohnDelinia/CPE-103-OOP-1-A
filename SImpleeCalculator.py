from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='First number')
        self.lbl2 = Label(win, text='Second number')
        self.lbl3 = Label(win, text='Result')
        self.t1 = Entry(bd=5)
        self.t2 = Entry(bd=5)
        self.t3 = Entry(bd=5)
        self.btn1 = Button(win, text='Add', command=self.add)
        self.btn2 = Button(win, text='Subtract', command=self.sub)

        # Place labels, entries, and buttons
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.btn1.place(x=100, y=150)
        self.btn2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.calculate(self.add_operation)

    def sub(self):
        self.calculate(self.sub_operation)

    def calculate(self, operation):
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            result = operation(num1, num2)
            self.display_result(result)
        except ValueError:
            self.display_error("Invalid input!")

    def add_operation(self, num1, num2):
        return num1 + num2

    def sub_operation(self, num1, num2):
        return num1 - num2

    def display_result(self, result):
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(result))

    def display_error(self, message):
        self.t3.delete(0, 'end')
        self.t3.insert(END, message)


# Create the main window
window = Tk()
mywin = MyWindow(window)
window.title('Simple Calculator')
window.geometry("400x300+10+10")
window.mainloop()