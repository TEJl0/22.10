import tkinter as tk
import math

root = tk.Tk()
root.geometry("400x400")
root.title("Узор из кнопок")

n = 12
i = 0
while i < n:
    a = 2 * math.pi * i / n
    x = 180 + 120 * math.cos(a)
    y = 180 + 120 * math.sin(a)
    b = tk.Button(root, text=str(i), width=3, height=1)
    b.place(x=x, y=y)
    i = i + 1

root.mainloop()
