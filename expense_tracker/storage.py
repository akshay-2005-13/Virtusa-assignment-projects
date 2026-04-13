import csv
import os
from expense import Expense

DATA_FILE = "data/expenses.csv"
HEADERS = ["date", "amount", "category", "description"]


def initialize_file():
    if not os.path.exists(DATA_FILE):
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        print("Data file created successfully.")


def save_expense(expense):
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())


def load_all_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    
    expenses = []
    
    with open(DATA_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                expense = Expense.from_dict(row)
                expenses.append(expense)
            except (ValueError, KeyError):
                continue
    
    return expenses


def delete_expense(index):
    expenses = load_all_expenses()
    
    if index < 0 or index >= len(expenses):
        print("Invalid index. No expense deleted.")
        return False
    
    expenses.pop(index)
    
    with open(DATA_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)
        for expense in expenses:
            writer.writerow(expense.to_list())
    
    return True


def get_total_count():
    expenses = load_all_expenses()
    return len(expenses)