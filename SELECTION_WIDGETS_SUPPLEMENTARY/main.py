import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Birth Date Selection')
window.geometry('500x350')

window.iconbitmap('account-circle_119476.ico')

def show_birth_info():
    birth_month = month_combobox.get()
    birth_day = day_combobox.get()
    birth_year = year_combobox.get()
    showinfo(
        title="Birth Information",
        message=f'You selected: {birth_month} {birth_day}, {birth_year}')

ttk.Label(window, text="Choose Your Birth Month",
          background='light yellow', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1, pady=10)

ttk.Label(window, text="Select The Month Of Your Birth:",
          font=("Times New Roman", 12)).grid(column=0, row=1, padx=5, pady=10)

month_combobox = ttk.Combobox(window, width=27)
month_combobox['values'] = (' January', ' February', ' March', ' April', ' May', ' June', ' July', ' August',
                            ' September', ' October', ' November', ' December')
month_combobox.grid(column=1, row=1)
month_combobox.current(0)

ttk.Label(window, text="Select The Day Of Your Birth (DD):",
          font=("Times New Roman", 12)).grid(column=0, row=2, padx=5, pady=10)

day_combobox = ttk.Combobox(window, width=27)
day_combobox['values'] = [f' {i}' for i in range(1, 32)]
day_combobox.grid(column=1, row=2)
day_combobox.current(0)

ttk.Label(window, text="Select The Year Of Your Birth (YYYY):",
          font=("Times New Roman", 12)).grid(column=0, row=3, padx=5, pady=10)

year_combobox = ttk.Combobox(window, width=27)
year_combobox['values'] = [str(year) for year in range(1900, 2026)]
year_combobox.grid(column=1, row=3)
year_combobox.current(0)

ttk.Button(window, text="Show Birth Information", command=show_birth_info).grid(column=1, row=4, pady=20)

window.mainloop()