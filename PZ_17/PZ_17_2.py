#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ № 2

import tkinter as tk
from tkinter import messagebox
def process_number():
    try:
        num = int(entry.get())
        if 100 <= num <= 999:
            last_digit = num % 10
            middle_digit = (num // 10) % 10
            result = f"Последняя цифра: {last_digit}\nСредняя цифра: {middle_digit}"
            messagebox.showinfo("Результат", result)
        else:
            messagebox.showwarning("Ошибка", "Введите трехзначное число!")
    except ValueError:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите число.")
root = tk.Tk()
root.title("Обработка числа")
tk.Label(root, text="Введите трёхзначное число:").pack()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="Обработать", command=process_number)
btn.pack()
root.mainloop()