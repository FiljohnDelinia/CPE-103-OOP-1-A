from datetime import timedelta

# Constants for file names and class duration
STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"
CLASS_DURATION = timedelta(hours=4)

# Style dictionaries for various UI elements
frame_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#FFFFFF",
    "fg": "#2E8B57",
    "bd": 2,
    "relief": "groove",
    "highlightbackground": "#2E8B57"
}

button_style = {
    "font": ("Arial", 11, "bold"),
    "fg": "#FFFFFF",
    "height": 2,
    "bd": 0,
    "activebackground": "#FF8C00"
}
