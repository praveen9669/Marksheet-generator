from tkinter import *
from tkinter import messagebox
import pdf


def click():
    if name_e.get() and sec_e.get() and sub_e.get():
        Label(frame, text="  ", font=("arial", 5)).grid(row=9, column=0, pady=5)
        
        Label(frame, text="Enter no of students:").grid(row=10, column=0, pady=5)
        global std_e
        std_e = Entry(frame)
        std_e.grid(row=10, column=1, pady=5)

        Label(frame, text="Enter Starting Roll No:").grid(row=12, column=0, pady=5)
        global roll_e
        roll_e = Entry(frame)
        roll_e.grid(row=12, column=1, pady=5)

        Button(frame, text="Submit", command=clicked).grid(row=14, column=0, columnspan=2, pady=5)
        update_scroll_region()

    else:
        messagebox.showinfo("Warning", "Fill all the details")

def clicked():
    if std_e.get() and roll_e.get():
        no_std = int(std_e.get())
        roll_no = int(roll_e.get())
        global student_data
        student_data = {
    "Branch": name_e.get(),
    "Section": sec_e.get(),
    "Subject": sub_e.get(),
    "roll_no": [],
    "Marks": []
        }
        entry_list = []  # Store entry widgets for navigation
        for i in range(no_std):
            roll = roll_no + i
            Label(frame, text=f"Enter marks for {roll}:").grid(row=15 + i, column=0, padx=10, pady=5)
            student_data["roll_no"].append(roll)
            sec_entry = Entry(frame)
            student_data["Marks"].append(sec_entry)
            sec_entry.grid(row=15 + i, column=1, padx=10, pady=5)
              # Store entry widget reference
            entry_list.append(sec_entry)

        # Set Enter key navigation
        for i in range(len(entry_list) - 1):
            entry_list[i].bind("<Return>", lambda event, e=entry_list[i+1]: e.focus())
        entry_list[-1].bind("<Return>", lambda event: submit_marks())

        # Submit buttons
        Button(frame, text="Submit Marks", command=submit_marks).grid(row=100, column=0, columnspan=2, pady=10)
        Button(frame, text="Print PDF", command=lambda: pdf.listpdf("marksheet.pdf", student_data)).grid(row=104, column=0, columnspan=2, pady=5)
        
        update_scroll_region()
    else:
        messagebox.showwarning("Warning", "Fill all the details")

def submit_marks():

    # Convert Entry fields to actual values
    
    for i in range(len(student_data["Marks"])):
        student_data["Marks"][i] = int(student_data["Marks"][i].get())  # Extract entered values
    messagebox.showinfo("Success", "Marks entered successfully!")
    print(student_data)
def update_scroll_region():
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Main Tkinter Window
root = Tk()
root.title("GUI Form")
root.geometry("500x650")

# Scrollable Canvas
canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=scrollbar.set)

# Scrollable Frame inside Canvas
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Header
Label(frame, text="\nSATHYABAMA\n", font=("arial", 22), width=20).grid(row=0, column=0, columnspan=2)

# Branch Input
Label(frame, text="BRANCH :", font=("arial", 10)).grid(row=2, column=0, pady=10)
name_e = Entry(frame)
name_e.grid(row=2, column=1, pady=10)

# Section Input
Label(frame, text="SECTION :", font=("arial", 10)).grid(row=4, column=0, pady=10)
sec_e = Entry(frame)
sec_e.grid(row=4, column=1, pady=10)

# Subject Input
Label(frame, text="SUBJECT :", font=("arial", 10)).grid(row=6, column=0, pady=10)
sub_e = Entry(frame)
sub_e.grid(row=6, column=1, pady=10)

# Submit Button
Button(frame, text="Submit", command=click).grid(row=8, column=0, columnspan=2, pady=10)

# Update Scrollbar Initially
update_scroll_region()

root.mainloop()
