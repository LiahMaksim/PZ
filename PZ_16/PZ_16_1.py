#Блок задания 1:
#Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
#Добавьте методы для вычисления процентных начислений и снятия денег.

import sqlite3
import csv

class Bank:
    def __init__(self, initial_amount, interest_rate):
        self.balance = initial_amount
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        return interest
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class ProductionCostsDB:
    def __init__(self, db_name='production_costs.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Expenses
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             Date TEXT NOT NULL,
                             ProductCode TEXT NOT NULL,
                             ProductName TEXT NOT NULL,
                             ExpenseType TEXT NOT NULL,
                             Amount REAL NOT NULL)''')
        self.conn.commit()
    
    def add_expense(self, date, product_code, product_name, expense_type, amount):
        self.cursor.execute('''INSERT INTO Expenses 
                            (Date, ProductCode, ProductName, ExpenseType, Amount)
                            VALUES (?, ?, ?, ?, ?)''',
                          (date, product_code, product_name, expense_type, amount))
        self.conn.commit()
    
    def get_all_expenses(self):
        self.cursor.execute('''SELECT * FROM Expenses ORDER BY Date DESC''')
        return self.cursor.fetchall()
    
    def get_expenses_by_product(self, product_code):
        self.cursor.execute('''SELECT Date, ExpenseType, Amount 
                            FROM Expenses 
                            WHERE ProductCode = ? 
                            ORDER BY Date''', (product_code,))
        return self.cursor.fetchall()
    
    def get_total_expenses_by_product(self):
        self.cursor.execute('''SELECT ProductCode, ProductName, SUM(Amount) as Total
                            FROM Expenses
                            GROUP BY ProductCode
                            ORDER BY Total DESC''')
        return self.cursor.fetchall()
    
    def get_expenses_by_date_range(self, start_date, end_date):
        self.cursor.execute('''SELECT * FROM Expenses 
                            WHERE Date BETWEEN ? AND ?
                            ORDER BY Date''', (start_date, end_date))
        return self.cursor.fetchall()
    
    def update_expense(self, expense_id, new_amount):
        self.cursor.execute('''UPDATE Expenses 
                            SET Amount = ?
                            WHERE id = ?''', (new_amount, expense_id))
        self.conn.commit()
    
    def export_to_csv(self, filename):
        self.cursor.execute('''SELECT * FROM Expenses''')
        expenses = self.cursor.fetchall()
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Дата', 'Код продукта', 'Наименование', 'Тип расхода', 'Сумма'])
            writer.writerows(expenses)
    
    def close(self):
        self.conn.close()
