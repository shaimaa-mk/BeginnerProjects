import tkinter as tk
from tkinter import ttk

# Initiate GUI for calculator
# root window
root = tk.Tk()
root.title("Calculator")
root.geometry('440x170')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)

# filed options
options = {'padx': 5, 'pady': 5}

# Number labels
first = ttk.Label(frame, text='First Number')
first.grid(column=0, row=0, sticky='w', **options)

second = ttk.Label(frame, text='Second Number')
second.grid(column=0, row=1, sticky='w', **options)

# Number entries
first_num = tk.StringVar()
first_num_entry = ttk.Entry(frame, textvariable=first_num)
first_num_entry.grid(column=1, row=0, **options)
first_num_entry.focus()

second_num = tk.StringVar()
second_num_entry = ttk.Entry(frame, textvariable=second_num)
second_num_entry.grid(column=1, row=1, **options)
second_num_entry.focus()

# Operation Buttons

# Addition


def add_opr():
    try:
        fnum = float(first_num.get())
        snum = float(second_num.get())
        add = fnum + snum
        result = str(add)
        result_label.config(text=result)
    except ValueError:
        print("Invalid Value")


add_button = ttk.Button(frame, text='Addition')
add_button.grid(column=0, row=5, sticky='w', **options)
add_button.config(command=add_opr)

# Subtraction


def sub_pre():
    try:
        fnum = float(first_num.get())
        snum = float(second_num.get())
        sub = fnum - snum
        result = str(sub)
        result_label.config(text=result)
    except ValueError:
        print("Invalid Value")


sub_button = ttk.Button(frame, text='Subtraction')
sub_button.grid(column=1, row=5, **options)
sub_button.config(command=sub_pre)

# # Multiplication


def multi_por():
    try:
        fnum = float(first_num.get())
        snum = float(second_num.get())
        multi = fnum * snum
        result = str(multi)
        result_label.config(text=result)
    except ValueError:
        print("Invalid Value")


multi_button = ttk.Button(frame, text='Multiplication')
multi_button.grid(column=3, row=5, **options)
multi_button.config(command=multi_por)


# Result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=2, **options)

frame.grid(padx=20, pady=20)

# Start the App
root.mainloop()
