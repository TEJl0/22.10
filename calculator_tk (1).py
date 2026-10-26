#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

current_input = ""
first_number = None
operator = None


def update_display():
    if current_input == "":
        text_input.config(text="0")
    else:
        text_input.config(text=current_input)


def on_button_click(value):
    global current_input, first_number, operator

    if value in "0123456789":
        current_input = current_input + value
        update_display()

    elif value == "+":
        if current_input != "":
            first_number = float(current_input)
            operator = "+"
            current_input = ""
            text_input.config(text=str(first_number) + " +")

    elif value == "-":
        if current_input != "":
            first_number = float(current_input)
            operator = "-"
            current_input = ""
            text_input.config(text=str(first_number) + " -")

    elif value == "*":
        if current_input != "":
            first_number = float(current_input)
            operator = "*"
            current_input = ""
            text_input.config(text=str(first_number) + " *")

    elif value == "/":
        if current_input != "":
            first_number = float(current_input)
            operator = "/"
            current_input = ""
            text_input.config(text=str(first_number) + " /")

    elif value == "=":
        if first_number is not None and operator is not None and current_input != "":
            second_number = float(current_input)
            result = 0.0

            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                if second_number == 0:
                    text_input.config(text="Ошибка: деление на 0")
                    current_input = ""
                    first_number = None
                    operator = None
                    return
                else:
                    result = first_number / second_number

            if result == int(result):
                current_input = str(int(result))
            else:
                current_input = str(result)

            text_input.config(text=current_input)
            first_number = None
            operator = None


root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x420")
root.resizable(False, False)

text_input = tk.Label(
    root,
    text="0",
    font=("Arial", 24),
    bg="#e0e0e0",
    anchor="e",
    padx=10,
    pady=15,
    width=15
)
text_input.pack(pady=10, padx=10, fill="x")

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

operations = ["+", "-", "*", "/", "="]

digit_buttons = []
for i in range(10):
    btn = tk.Button(
        buttons_frame,
        text=str(i),
        font=("Arial", 16),
        width=4,
        height=2,
        command=lambda v=str(i): on_button_click(v)
    )
    digit_buttons.append(btn)

digit_buttons[7].grid(row=0, column=0, padx=3, pady=3)
digit_buttons[8].grid(row=0, column=1, padx=3, pady=3)
digit_buttons[9].grid(row=0, column=2, padx=3, pady=3)

digit_buttons[4].grid(row=1, column=0, padx=3, pady=3)
digit_buttons[5].grid(row=1, column=1, padx=3, pady=3)
digit_buttons[6].grid(row=1, column=2, padx=3, pady=3)

digit_buttons[1].grid(row=2, column=0, padx=3, pady=3)
digit_buttons[2].grid(row=2, column=1, padx=3, pady=3)
digit_buttons[3].grid(row=2, column=2, padx=3, pady=3)

digit_buttons[0].grid(row=3, column=0, columnspan=2, padx=3, pady=3, sticky="we")

op_buttons = []
for op in operations:
    btn = tk.Button(
        buttons_frame,
        text=op,
        font=("Arial", 16),
        width=4,
        height=2,
        bg="#f0a040",
        command=lambda v=op: on_button_click(v)
    )
    op_buttons.append(btn)

op_buttons[0].grid(row=0, column=3, padx=3, pady=3)
op_buttons[1].grid(row=1, column=3, padx=3, pady=3)
op_buttons[2].grid(row=2, column=3, padx=3, pady=3)
op_buttons[3].grid(row=3, column=2, padx=3, pady=3)
op_buttons[4].grid(row=3, column=3, padx=3, pady=3)

root.mainloop()
