import json
import os
from typing import Any, Dict, List

class Expense:
    title: str
    amount: float
    category: str

    def __init__(self, title: str, amount: float, category: str) -> None:
        self.title = title
        self.amount = amount
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """Перетворює об'єкт витрати у словник для збереження в JSON."""
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category
        }

    @staticmethod
    def load_expenses(filename: str = "expenses.json") -> List['Expense']:
        """Завантажує витрати з JSON файлу."""
        if not os.path.exists(filename):
            return []
        
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data: Any = json.load(file)
                if not isinstance(data, list):
                    return []
                
                expenses: List['Expense'] = []
                for item in data:
                    if isinstance(item, dict) and "title" in item and "amount" in item and "category" in item:
                        expenses.append(Expense(str(item["title"]), float(item["amount"]), str(item["category"])))
                return expenses
        except (json.JSONDecodeError, ValueError):
            return []

    @staticmethod
    def save_expenses(expenses: List['Expense'], filename: str = "expenses.json") -> None:
        """Зберігає список витрат у JSON файл."""
        with open(filename, "w", encoding="utf-8") as file:
            data: List[Dict[str, Any]] = [expense.to_dict() for expense in expenses]
            json.dump(data, file, ensure_ascii=False, indent=4)