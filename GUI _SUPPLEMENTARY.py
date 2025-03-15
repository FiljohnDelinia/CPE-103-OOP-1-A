import tkinter as tk
import math

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
        update_history(f"{entry1.get()} + {entry2.get()} = {result.get()}")
        error_label.config(text="")
    except ValueError:
        error_label.config(text="Error! Invalid input.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
        update_history(f"{entry1.get()} - {entry2.get()} = {result.get()}")
        error_label.config(text="")
    except ValueError:
        error_label.config(text="Error! Invalid input.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
        update_history(f"{entry1.get()} × {entry2.get()} = {result.get()}")
        error_label.config(text="")
    except ValueError:
        error_label.config(text="Error! Invalid input.")

def divide():
    try:
        divisor = float(entry2.get())
        if divisor == 0:
            raise ZeroDivisionError
        result.set(float(entry1.get()) / divisor)
        update_history(f"{entry1.get()} ÷ {entry2.get()} = {result.get()}")
        error_label.config(text="")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
        error_label.config(text="Error! Division by zero.")
    except ValueError:
        result.set("Error! Invalid input.")
        error_label.config(text="Error! Invalid input.")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            raise ValueError("Cannot take the square root of a negative number")
        result.set(math.sqrt(num))
        update_history(f"√{num} = {result.get()}")
        error_label.config(text="")
    except ValueError as e:
        result.set(f"Error! {e}")
        error_label.config(text=f"Error! {e}")

def power():
    try:
        result.set(float(entry1.get()) ** float(entry2.get()))
        update_history(f"{entry1.get()} ^ {entry2.get()} = {result.get()}")
        error_label.config(text="")
    except ValueError:
        result.set("Error! Invalid input.")
        error_label.config(text="Error! Invalid input.")

def sine():
    try:
        num = float(entry1.get())
        result.set(math.sin(math.radians(num)))
        update_history(f"sin({num}) = {result.get()}")
        error_label.config(text="")
    except ValueError:
        result.set("Error! Invalid input.")
        error_label.config(text="Error! Invalid input.")

def cosine():
    try:
        num = float(entry1.get())
        result.set(math.cos(math.radians(num)))
        update_history(f"cos({num}) = {result.get()}")
        error_label.config(text="")
    except ValueError:
        result.set("Error! Invalid input.")
        error_label.config(text="Error! Invalid input.")

def tangent():
    try:
        num = float(entry1.get())
        result.set(math.tan(math.radians(num)))
        update_history(f"tan({num}) = {result.get()}")
        error_label.config(text="")
    except ValueError:
        result.set("Error! Invalid input.")
        error_label.config(text="Error! Invalid input.")
    except Exception:
        result.set("Error! Invalid input.")
        error_label.config(text="Error! Invalid input.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
    error_label.config(text="")

def update_history(operation):
    history_list.insert(tk.END, operation)
    if len(history_list.get(0, tk.END)) > 10:
        history_list.delete(0)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#2E2E2E")

result = tk.StringVar()

tk.Label(root, text="Enter 1st number:", font=("Arial", 12), bg="#2E2E2E", fg="white").place(x=30, y=30)
entry1 = tk.Entry(root)
entry1.place(x=180, y=30, width=150)

tk.Label(root, text="Enter 2nd number:", font=("Arial", 12), bg="#2E2E2E", fg="white").place(x=30, y=80)
entry2 = tk.Entry(root)
entry2.place(x=180, y=80, width=150)

tk.Button(root, text="+", command=add, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=30, y=130)
tk.Button(root, text="-", command=subtract, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=180, y=130)
tk.Button(root, text="x", command=multiply, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=30, y=180)
tk.Button(root, text="/", command=divide, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=180, y=180)

tk.Button(root, text="√", command=square_root, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=30, y=230)
tk.Button(root, text="^", command=power, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=180, y=230)
tk.Button(root, text="sin", command=sine, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=30, y=280)
tk.Button(root, text="cos", command=cosine, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=180, y=280)
tk.Button(root, text="tan", command=tangent, width=10, height=2, font=("Arial", 10), bg="black", fg="white").place(x=30, y=330)

tk.Button(root, text="Clear", command=clear, width=22, height=2, font=("Arial", 10), bg="#FF4500", fg="white").place(x=30, y=380)

# Result display
tk.Label(root, text="Result:", font=("Arial", 12, "bold"), bg="#000000", fg="#39FF14").place(x=30, y=430)
result_label = tk.Label(root, textvariable=result, font=("Arial", 12), bg="white", width=18, height=2, relief="sunken")
result_label.place(x=180, y=430)

error_label = tk.Label(root, text="", font=("Arial", 10), fg="red", bg="#2E2E2E")
error_label.place(x=30, y=480)

tk.Label(root, text="History:", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="#D3D3D3").place(x=30, y=510)
history_list = tk.Listbox(root, width=40, height=5, font=("Arial", 10))
history_list.place(x=30, y=540)

root.mainloop()