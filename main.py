import logging
from expense import Expense
from typing import List

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def main() -> None:
    logging.info("Програма 'Менеджер особистих витрат' запущена.")

    expenses: List[Expense] = Expense.load_expenses()

    while True:
        print("\n--- МЕНЕДЖЕР ВИТРАТ ---")
        print("1. Додати витрату")
        print("2. Показати всі витрати")
        print("3. Показати витрати за категорією")
        print("4. Показати загальну суму")
        print("5. Вийти")
        
        choice: str = input("Оберіть дію (1-5): ").strip()

        if choice == "1":
            print("\n[Додавання витрати]")
            title: str = input("Назва: ").strip()
            
            raw_amount: str = input("Сума: ").strip()
            try:
                amount: float = float(raw_amount)
            except ValueError:
                print("Помилка! Сума повинна бути числом.")
                logging.error(f"Помилка введення суми: користувач ввів '{raw_amount}', що не є числом.")
                continue
                
            category: str = input("Категорія: ").strip()

            new_expense: Expense = Expense(title, amount, category)
            expenses.append(new_expense)
            
            Expense.save_expenses(expenses)
            print("Витрату успішно додано!")
            logging.info(f"Додано нову витрату: {title} — {amount} грн (Категорія: {category}).")

        elif choice == "2":
            print("\n[Всі витрати]")
            logging.info("Користувач переглядає всі витрати.")
            if not expenses:
                print("Список витрат порожній.")
            else:
                for index, exp in enumerate(expenses, start=1):
                    print(f"{index}. {exp.title} {exp.amount} грн {exp.category}")

        elif choice == "3":
            print("\n[Фільтрація за категорією]")
            search_category: str = input("Введіть категорію для пошуку: ").strip()
            logging.info(f"Користувач запустив фільтрацію за категорією: '{search_category}'.")
            
            filtered: List[Expense] = [e for e in expenses if e.category.lower() == search_category.lower()]
            
            if not filtered:
                print(f"Витрат у категорії '{search_category}' не знайдено.")
            else:
                for index, exp in enumerate(filtered, start=1):
                    print(f"{index}. {exp.title} {exp.amount} грн {exp.category}")

        elif choice == "4":
            print("\n[Загальна сума]")
            total: float = sum(exp.amount for exp in expenses)
            print(f"Загальна сума витрат: {total} грн")
            logging.info(f"Переглянуто загальну суму витрат. Результат: {total} грн.")

        elif choice == "5":
            print("\nДякуємо, що користувалися програмою! Бувай!")
            logging.info("Програма завершила свою роботу за запитом користувача.")
            break
            
        else:
            print("Неправильний вибір! Будь ласка, введіть число від 1 до 5.")
            logging.warning(f"Користувач ввів неправильний пункт меню: '{choice}'.")

if __name__ == "__main__":
    main()