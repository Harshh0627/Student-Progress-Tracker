import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Student Progress Tracker")
root.geometry("400x500")
bg_color = "#f0f4f8"
root.config(bg=bg_color)


title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
title_label = tk.Label(root, text="Student Progress Tracker", font=title_font, bg=bg_color)
title_label.pack(pady=20)


name_label = tk.Label(root, text="Student Name:", font=label_font, bg=bg_color)
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

subject1_label = tk.Label(root, text="Subject 1 Marks:", font=label_font, bg=bg_color)
subject1_label.pack(pady=5)
subject1_entry = tk.Entry(root, width=30)
subject1_entry.pack(pady=5)

subject2_label = tk.Label(root, text="Subject 2 Marks:", font=label_font, bg=bg_color)
subject2_label.pack(pady=5)
subject2_entry = tk.Entry(root, width=30)
subject2_entry.pack(pady=5)

subject3_label = tk.Label(root, text="Subject 3 Marks:", font=label_font, bg=bg_color)
subject3_label.pack(pady=5)
subject3_entry = tk.Entry(root, width=30)
subject3_entry.pack(pady=5)


def calculate_progress():
    try:
        marks1 = int(subject1_entry.get())
        marks2 = int(subject2_entry.get())
        marks3 = int(subject3_entry.get())

        total = marks1 + marks2 + marks3
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        messagebox.showinfo("Result", f"Total: {total}\nPercentage: {percentage:.2f}%\nGrade: {grade}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all subjects.")


def reset_fields():
    name_entry.delete(0, tk.END)
    subject1_entry.delete(0, tk.END)
    subject2_entry.delete(0, tk.END)
    subject3_entry.delete(0, tk.END)


calculate_button = tk.Button(root, text="Calculate Progress", command=calculate_progress, bg="#4CAF50", fg="white", font=("Helvetica", 12))
calculate_button.pack(pady=20)

reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="#f44336", fg="white", font=("Helvetica", 12))
reset_button.pack(pady=10)


calculate_button.bind("<Enter>", lambda e: e.widget.config(background='#45a049'))
calculate_button.bind("<Leave>", lambda e: e.widget.config(background='#4CAF50'))

reset_button.bind("<Enter>", lambda e: e.widget.config(background='#e53935'))
reset_button.bind("<Leave>", lambda e: e.widget.config(background='#f44336'))

root.mainloop()
