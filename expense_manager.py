from file_handler import save_expenses
from expenses import Expense
def add_expense(expenses, expense):
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if expenses:
        for expense in expenses:
            print(expense)
            print()
    else:
        print("no expense data!")

def search_expense(expenses, keyword):
    results= [
        expense 
        for expense in expenses
        if keyword.lower() in expense.title.lower()
    ]
    if results:
        for expense in results:
            print(expense)
    else:
        print("No matching expenses found!")

def delete_expense(expenses):
    if not expenses:
        print("No expense to delete!")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense.summary()}")
    delete = int(input("Enter the number you want to remove: "))
    if 0< delete <= len(expenses):
        index = delete - 1
        expenses.pop(index)
        print("Expesne deleted successfully.")
    else:
        print("invalid choice")
    save_expenses(expenses)
        
