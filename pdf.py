from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import *
from tkinter import messagebox

def listpdf(filename, student_data):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Student Marksheet")

    # Set font for details
    c.setFont("Helvetica", 12)

    # Positioning variables
    x_start, y_start = 100, height - 100
    line_spacing = 20

    # Student details
    c.drawString(x_start, y_start, f"Branch : {student_data['Branch']}")
    c.drawString(x_start, y_start - line_spacing, f"Section : {student_data['Section']}")
    c.drawString(x_start, y_start - 2 * line_spacing, f"Subject : {student_data['Subject']}")

    # Subjects and Marks Table
    y_subjects_start = y_start - 4 * line_spacing
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_start, y_subjects_start, "Roll No")
    c.drawString(x_start + 200, y_subjects_start, "Marks")
    
    c.setFont("Helvetica", 12)
    for i, (roll, mark) in enumerate(zip(student_data["roll_no"], student_data["Marks"])):
        c.drawString(x_start, y_subjects_start - (i + 1) * line_spacing, str(roll))
        c.drawString(x_start + 200, y_subjects_start - (i + 1) * line_spacing, str(mark))

    # Save PDF
    c.save()
    messagebox.showinfo("Success", f"Marksheet saved as {filename}")

# Student data dictionary

