import tkinter as tk
from tkinter import messagebox

# ------------------------
# Button Functions
# ------------------------

def student_registration():
    messagebox.showinfo(
        "Student Registration",
        "Student Registration Module Opened"
    )

def course_enrollment():
    messagebox.showinfo(
        "Course Enrollment",
        "Course Enrollment Module Opened"
    )

def student_records():
    messagebox.showinfo(
        "Student Records",
        "Student Records Module Opened"
    )

def search_sort():
    messagebox.showinfo(
        "Search & Sort",
        "Search & Sort Module Opened"
    )

def fee_calculator():
    messagebox.showinfo(
        "Fee Calculator",
        "Fee Calculator Module Opened"
    )

def file_management():
    messagebox.showinfo(
        "File Handling",
        "File Handling Module Opened"
    )

def directory_scanner():
    messagebox.showinfo(
        "Directory Scanner",
        "Directory Scanner Module Opened"
    )

def analytics():
    messagebox.showinfo(
        "Performance Analytics",
        "Analytics Module Opened"
    )

# ------------------------
# Main Window
# ------------------------

root = tk.Tk()

root.title("Smart Campus Information System")

root.geometry("700x500")

root.resizable(False, False)

# Heading

heading = tk.Label(
    root,
    text="SMART CAMPUS INFORMATION SYSTEM",
    font=("Arial", 18, "bold")
)

heading.pack(pady=20)

# Buttons

tk.Button(
    root,
    text="1. Student Registration",
    width=30,
    command=student_registration
).pack(pady=5)

tk.Button(
    root,
    text="2. Course Enrollment",
    width=30,
    command=course_enrollment
).pack(pady=5)

tk.Button(
    root,
    text="3. Student Records",
    width=30,
    command=student_records
).pack(pady=5)

tk.Button(
    root,
    text="4. Search & Sort Student IDs",
    width=30,
    command=search_sort
).pack(pady=5)

tk.Button(
    root,
    text="5. Fee Calculator",
    width=30,
    command=fee_calculator
).pack(pady=5)

tk.Button(
    root,
    text="6. File Management",
    width=30,
    command=file_management
).pack(pady=5)

tk.Button(
    root,
    text="7. Directory Scanner",
    width=30,
    command=directory_scanner
).pack(pady=5)

tk.Button(
    root,
    text="8. Performance Analytics",
    width=30,
    command=analytics
).pack(pady=5)

tk.Button(
    root,
    text="Exit",
    width=30,
    command=root.destroy
).pack(pady=15)

root.mainloop()