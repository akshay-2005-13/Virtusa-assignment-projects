from datetime import datetime
from expense import Expense
import storage


def add_expense(date, amount, category, description):
    
    # Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date}. Use YYYY-MM-DD")
    
    # Validate amount
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
    except ValueError:
        raise ValueError("Amount must be a valid positive number")
    
    # Validate category
    if category not in Expense.CATEGORIES:
        raise ValueError(f"Invalid category. Choose from: {Expense.CATEGORIES}")
    
    # Validate description
    if not description.strip():
        raise ValueError("Description cannot be empty")
    
    expense = Expense(date, amount, category, description.strip())
    storage.save_expense(expense)
    return expense


def get_all_expenses():
    return storage.load_all_expenses()


def get_expenses_by_month(year, month):
    all_expenses = storage.load_all_expenses()
    
    month_str = f"{year}-{month:02d}"
    
    filtered = []
    for expense in all_expenses:
        if expense.date.startswith(month_str):
            filtered.append(expense)
    
    return filtered


def get_expenses_by_category(category):
    all_expenses = storage.load_all_expenses()
    
    filtered = []
    for expense in all_expenses:
        if expense.category.lower() == category.lower():
            filtered.append(expense)
    
    return filtered


def get_expenses_by_date_range(start_date, end_date):
    all_expenses = storage.load_all_expenses()
    
    filtered = []
    for expense in all_expenses:
        expense_date = datetime.strptime(expense.date, "%Y-%m-%d")
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        if start <= expense_date <= end:
            filtered.append(expense)
    
    return filtered


def get_total_spending(expenses):
    total = 0
    for expense in expenses:
        total += expense.amount
    return total


def delete_expense_by_index(index):
    return storage.delete_expense(index)


def get_current_month_expenses():
    now = datetime.now()
    return get_expenses_by_month(now.year, now.month)