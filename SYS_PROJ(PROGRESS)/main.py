import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta

STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"
CLASS_DURATION = timedelta(hours=4)

def register_student():
    student_id = entry_id.get()
    student_name = entry_name.get()

    if not student_id or not student_name:
        messagebox.showerror("Error", "Please enter both Student ID and Name")
        return

    with open(STUDENT_FILE, "a") as file:
        file.write(f"{student_id},{student_name}\n")

    messagebox.showinfo("Success", f"Student '{student_name}' registered!")
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)

def record_time():
    student_id = entry_attendance.get()

    with open(STUDENT_FILE, "r") as file:
        students = file.readlines()

    student_name = None
    for student in students:
        sid, name = student.strip().split(",")
        if sid == student_id:
            student_name = name
            break

    if student_name:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        today = datetime.now().strftime("%Y-%m-%d")

        attendance_records = []
        try:
            with open(ATTENDANCE_FILE, "r") as file:
                attendance_records = file.readlines()
        except FileNotFoundError:
            pass

        last_record = None
        for record in attendance_records:
            rec_id, rec_name, rec_time_in, rec_time_out = record.strip().split(",")
            if rec_id == student_id and rec_time_in.startswith(today):
                last_record = record.strip()

        if last_record and last_record.split(",")[3] == "":
            updated_records = []
            for record in attendance_records:
                if record.strip() == last_record:
                    updated_records.append(f"{student_id},{student_name},{last_record.split(',')[2]},{timestamp}\n")
                else:
                    updated_records.append(record)
            with open(ATTENDANCE_FILE, "w") as file:
                file.writelines(updated_records)
            messagebox.showinfo("Success", f"Time Out recorded for {student_name}")
        else:
            with open(ATTENDANCE_FILE, "a") as file:
                file.write(f"{student_id},{student_name},{timestamp},\n")
            messagebox.showinfo("Success", f"Time In recorded for {student_name}")
        entry_attendance.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Student ID not found")

def generate_daily_report():
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(ATTENDANCE_FILE, "r") as file:
            records = file.readlines()