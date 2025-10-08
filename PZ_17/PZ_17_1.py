#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Создайте заказ")
root.geometry("600x520")
root.resizable(False, False)

header_frame = tk.Frame(root, bg="#55606e")
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="Создайте заказ", font=("Arial", 15), fg="white", bg="#55606e", pady=8)
header_label.pack()

form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(fill="both", expand=True)

section1 = tk.LabelFrame(form_frame, text="Информация о заказе", font=("Arial", 11, "bold"), padx=10, pady=10)
section1.pack(fill="x", pady=(0, 10))

tk.Label(section1, text="Номер заказа *").grid(row=0, column=0, sticky="w")
order_entry = tk.Entry(section1, width=40)
order_entry.grid(row=0, column=1, padx=12, pady=2)

tk.Label(section1, text="Название товара").grid(row=1, column=0, sticky="w")
item_entry = tk.Entry(section1, width=40)
item_entry.grid(row=1, column=1, padx=12, pady=2)

tk.Label(section1, text="Количество *").grid(row=2, column=0, sticky="w")
qty_entry = tk.Entry(section1, width=40)
qty_entry.grid(row=2, column=1, padx=12, pady=2)

section2 = tk.LabelFrame(form_frame, text="Контактная информация", font=("Arial", 11, "bold"), padx=10, pady=10)
section2.pack(fill="x", pady=(0, 10))

tk.Label(section2, text="Ваше имя").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(section2, width=40)
name_entry.grid(row=0, column=1, padx=12, pady=2)

tk.Label(section2, text="Ваш email *").grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(section2, width=40)
email_entry.grid(row=1, column=1, padx=12, pady=2)

tk.Label(section2, text="Ваш телефон *").grid(row=2, column=0, sticky="w")
phone_entry = tk.Entry(section2, width=40)
phone_entry.grid(row=2, column=1, padx=12, pady=2)
tk.Label(section2, text="Формат: +7 (999) 999-99-99", font=("Arial", 8), fg="gray").grid(row=3, column=1, sticky="w")

section3 = tk.LabelFrame(form_frame, text="Информация о доставке", font=("Arial", 11, "bold"), padx=10, pady=10)
section3.pack(fill="x", pady=(0, 10))

tk.Label(section3, text="Адрес *").grid(row=0, column=0, sticky="nw")
address_entry = tk.Text(section3, width=38, height=3)
address_entry.grid(row=0, column=1, padx=12, pady=2)

tk.Label(section3, text="Время доставки").grid(row=1, column=0, sticky="w", pady=10)
hours = ttk.Combobox(section3, values=[f"{i:02d}" for i in range(24)], width=2)
hours.grid(row=1, column=1, sticky="w", padx=(0,5), pady=10)
minutes = ttk.Combobox(section3, values=[f"{i:02d}" for i in range(0,60,5)], width=2)
minutes.grid(row=1, column=1, sticky="w", padx=(50,0), pady=10)

root.mainloop()