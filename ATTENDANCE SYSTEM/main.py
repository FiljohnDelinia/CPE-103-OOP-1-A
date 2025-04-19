import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta

STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"
CLASS_DURATION = timedelta(hours=4)

frame_style = {
    "font": ("Arial", 12, "bold"), "bg": "#FFFFFF", "fg": "#2E8B57", "bd": 2, "relief": "groove",
    "highlightbackground": "#2E8B57"
}

button_style = {
    "font": ("Arial", 11, "bold"), "fg": "#FFFFFF", "height": 2, "bd": 0, "activebackground": "#FF8C00"
}


def create_labeled_entry(parent, label_text):
    row = tk.Frame(parent, bg="#FFFFFF")
    row.pack(fill="x", padx=10, pady=5)
    tk.Label(row, text=label_text, font=("Arial", 11), bg="#FFFFFF", width=15, anchor="w").pack(side="left")
    entry = tk.Entry(row, font=("Arial", 11), relief="solid", borderwidth=1)
    entry.pack(side="right", expand=True, fill="x")
    return entry


def register_student():
    student_id = entry_id.get().strip()
    student_name = entry_name.get().strip()
    if not student_id or not student_name:
        messagebox.showerror("Error", "Please enter both Student ID and Name")
        return

    with open(STUDENT_FILE, "a+") as file:
        file.seek(0)
        students = file.readlines()

        # Check if the student ID already exists in the file
        for student in students:
            parts = student.strip().split(",")
            if len(parts) == 2:  # Ensure that each line has exactly 2 values
                stu_id, name = parts
                if stu_id == student_id:
                    messagebox.showerror("Error", f"Student ID '{student_id}' already exists!")
                    return

        # If student ID is not found, register the new student
        file.write(f"{student_id},{student_name}\n")
    messagebox.showinfo("Success", f"Student '{student_name}' registered!")
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)


def record_time():
    student_id = entry_attendance.get().strip()
    if not student_id:
        messagebox.showerror("Error", "Please enter a Student ID")
        return

    with open(STUDENT_FILE, "r") as file:
        students = file.readlines()

    # Only unpack lines with exactly two values
    student_name = next(
        (name for stu_id, name in (line.strip().split(",") for line in students if len(line.strip().split(",")) == 2) if
         stu_id == student_id), None)

    if not student_name:
        messagebox.showerror("Error", "Student ID not found")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.now().strftime("%Y-%m-%d")

    try:
        with open(ATTENDANCE_FILE, "r") as file:
            attendance_records = file.readlines()
    except FileNotFoundError:
        attendance_records = []

    last_index = None
    for i in reversed(range(len(attendance_records))):
        parts = attendance_records[i].strip().split(",")
        if len(parts) == 4 and parts[0] == student_id and parts[2].startswith(today) and parts[3] == "":
            last_index = i
            break

    if last_index is not None:
        parts = attendance_records[last_index].strip().split(",")
        parts[3] = timestamp
        attendance_records[last_index] = ",".join(parts) + "\n"
        with open(ATTENDANCE_FILE, "w") as file:
            file.writelines(attendance_records)
        messagebox.showinfo("Success", f"Time Out recorded for {student_name}")
    else:
        with open(ATTENDANCE_FILE, "a") as file:
            file.write(f"{student_id},{student_name},{timestamp},\n")
        messagebox.showinfo("Success", f"Time In recorded for {student_name}")

    entry_attendance.delete(0, tk.END)


def generate_daily_report():
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(ATTENDANCE_FILE, "r") as file:
            records = file.readlines()
        daily_records = []
        for record in records:
            fields = record.strip().split(",")
            if len(fields) == 4 and fields[2].startswith(today):
                time_in = datetime.strptime(fields[2], "%Y-%m-%d %H:%M:%S")
                time_out = datetime.strptime(fields[3], "%Y-%m-%d %H:%M:%S") if fields[3] else None
                fields.append("Incomplete Attendance" if not time_out or (
                            time_out - time_in) < CLASS_DURATION else "Complete Attendance")
                daily_records.append(",".join(fields))
        if not daily_records:
            messagebox.showinfo("Info", "No attendance records for today.")
            return
        with open(f"daily_report_{today}.csv", "w") as file:
            file.write("Student ID,Name,Time In,Time Out,Status\n")
            file.writelines("\n".join(daily_records) + "\n")
        messagebox.showinfo("Success", f"Daily report saved as daily_report_{today}.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "No attendance records found")


def view_filtered_attendance(date_filter=None, id_filter=None):
    # Use default empty string if date_filter or id_filter is None
    filter_date = date_filter.get().strip() if date_filter else ""
    filter_id = id_filter.get().strip() if id_filter else ""

    # Clear existing entries in the table
    for row in tree.get_children():
        tree.delete(row)

    try:
        with open(ATTENDANCE_FILE, "r") as file:
            records = file.readlines()

        for record in records:
            fields = record.strip().split(",")
            if len(fields) >= 3:
                time_in_out = f"{fields[2]} - {fields[3] if len(fields) > 3 and fields[3] else 'Not Out'}"

                # Apply both filters if provided
                if (not filter_date or fields[2].startswith(filter_date)) and (not filter_id or fields[0] == filter_id):
                    tree.insert("", tk.END, values=(fields[0], fields[1], time_in_out))

    except Exception as e:
        messagebox.showerror("Error", f"Failed to filter records: {e}")

def delete_student():
    student_id = entry_delete_id.get().strip()
    if not student_id:
        messagebox.showerror("Error", "Please enter a Student ID")
        return

    try:
        # Read all students into memory
        with open(STUDENT_FILE, "r") as file:
            students = file.readlines()

        # Filter out the student with the given ID
        students = [student for student in students if student.split(",")[0] != student_id]

        # If the student was not found
        if len(students) == len(open(STUDENT_FILE).readlines()):
            messagebox.showerror("Error", f"Student ID '{student_id}' not found.")
            return

        # Write the updated list back to the file
        with open(STUDENT_FILE, "w") as file:
            file.writelines(students)

        messagebox.showinfo("Success", f"Student with ID '{student_id}' deleted successfully!")
        entry_delete_id.delete(0, tk.END)
    except FileNotFoundError:
        messagebox.showerror("Error", "No students file found")

def clear_attendance():
    with open(ATTENDANCE_FILE, "w") as file:
        file.truncate()
    messagebox.showinfo("Success", "All attendance records have been cleared!")


def view_attendance():
    view_filtered_attendance()


def update_time():
    clock_label.config(text=f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    root.after(1000, update_time)


# GUI starts here
root = tk.Tk()
root.title("UCC College of Engineering Attendance System")
root.geometry("1000x800")

try:
    bg_image = Image.open("475059197_122184644036263173_8361834046506423414_n.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS))
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except:
    pass

clock_label = tk.Label(root, font=("Arial", 12, "bold"), bg="#FFE4B5", fg="#2E8B57")
clock_label.pack(anchor="nw", padx=30, pady=10)
update_time()

control_panel = tk.Frame(root, bg="#FFE4B5", width=350)
control_panel.pack(side="left", fill="y", padx=30, pady=7)

header_frame = tk.Frame(control_panel, bg="#FF8C00")
header_frame.pack(fill="x", pady=(0, 10))

tk.Label(header_frame,
         text="UNIVERSITY OF CALOOCAN CITY\nCOLLEGE OF ENGINEERING",
         font=("Arial", 14, "bold"),
         bg="#FF8C00",
         fg="#FFFFFF").pack()

tk.Label(header_frame,
         text="ATTENDANCE SYSTEM",
         font=("Arial", 12, "bold"),
         bg="#FF8C00",
         fg="#FFD700").pack(pady=5)

# Frames
reg_frame = tk.LabelFrame(control_panel, text="Student Registration", **frame_style)
att_frame = tk.LabelFrame(control_panel, text="Attendance Recording", **frame_style)
manage_frame = tk.LabelFrame(control_panel, text="Attendance Management", **frame_style)
table_frame = tk.LabelFrame(control_panel, text="Attendance Records", **frame_style)

reg_frame.pack(fill="x", pady=5)
att_frame.pack(fill="x", pady=5)
manage_frame.pack(fill="x", pady=5)
table_frame.pack(fill="both", expand=True, pady=5, ipady=5)

# Inputs must be created BEFORE used
entry_id = create_labeled_entry(reg_frame, "Student ID:")
entry_name = create_labeled_entry(reg_frame, "Student Name:")

tk.Button(reg_frame, text="Register Student", command=register_student, bg="#2E8B57", **button_style).pack(fill="x",
                                                                                                           padx=10,
                                                                                                           pady=5)

entry_attendance = create_labeled_entry(att_frame, "Enter Student ID:")
tk.Button(att_frame, text="Record Time In/Out", command=record_time, bg="#2E8B57", **button_style).pack(fill="x",
                                                                                                        padx=10, pady=5)

tk.Button(manage_frame, text="View Attendance", command=view_attendance, bg="#FF8C00", **button_style).pack(fill="x",
                                                                                                            padx=10,
                                                                                                            pady=5)
tk.Button(manage_frame, text="Generate Daily Report", command=generate_daily_report, bg="#2E8B57", **button_style).pack(
    fill="x", padx=10, pady=5)
tk.Button(manage_frame, text="Clear All Records", command=clear_attendance, bg="#8B0000", **button_style).pack(fill="x",
                                                                                                               padx=10,
                                                                                                               pady=5)

tree_container = tk.Frame(table_frame)
tree_container.pack(fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#FF8C00", foreground="#FFFFFF",
                relief="flat")
style.configure("Treeview", font=("Arial", 11), rowheight=40, background="#FFFFFF", fieldbackground="#FFFFFF",
                foreground="#2E8B57")
style.map("Treeview", background=[("selected", "#2E8B57")], foreground=[("selected", "#FFFFFF")])

tree = ttk.Treeview(tree_container, columns=("ID", "Name", "Time"), show="headings", selectmode="browse")

vsb = ttk.Scrollbar(tree_container, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(tree_container, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(row=0, column=0, sticky="nsew")
vsb.grid(row=0, column=1, sticky="ns")
hsb.grid(row=1, column=0, sticky="ew")

tree_container.grid_rowconfigure(0, weight=1)
tree_container.grid_columnconfigure(0, weight=1)

tree.heading("ID", text="Student ID", anchor="center")
tree.heading("Name", text="Name", anchor="center")
tree.heading("Time", text="Time In/Out", anchor="center")
tree.column("ID", width=120, anchor="center", stretch=False)
tree.column("Name", width=180, anchor="w", stretch=False)
tree.column("Time", width=300, anchor="center", stretch=True)

root.mainloop()
