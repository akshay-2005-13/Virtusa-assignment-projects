from datetime import datetime

class Expense:
    
    CATEGORIES = [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Health",
        "Education",
        "Bills",
        "Other"
    ]
    
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = float(amount)
        self.category = category
        self.description = description
    
    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
    
    def to_list(self):
        return [self.date, self.amount, self.category, self.description]
    
    @classmethod
    def from_dict(cls, row):
        return cls(
            date=row["date"],
            amount=float(row["amount"]),
            category=row["category"],
            description=row["description"]
        )
    
    def __str__(self):
        return (f"{self.date} | "
                f"{self.category:<15} | "
                f"Rs.{self.amount:>10.2f} | "
                f"{self.description}")