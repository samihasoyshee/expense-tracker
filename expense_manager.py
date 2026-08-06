from file_handler import save_expenses
from expenses import Expense
def add_expense(expenses, expense):
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if expenses:
         for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense}")
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
        print(f"{index}. {expense}")
    delete = int(input("Enter the number you want to remove: "))
    if 0< delete <= len(expenses):
        index = delete - 1
        expenses.pop(index)
        print("Expesne deleted successfully.")
    else:
        print("invalid choice")
    save_expenses(expenses)

def view_summary(expenses):
    total = 0
    category_totals = {}
    for expense in expenses:
        total += expense.amount    
        
        category = expense.category
        if category in category_totals:
            category_totals[category] += expense.amount
        else:
            category_totals[category] = expense.amount

    print(f"Total Expense: {total}")

    print("\nExpenses by Category")
    for category, amount in category_totals.items():
        print(f"{category}: {amount}")

def edit_expense(expenses):
    view_expenses(expenses)
    choice = int(input("Enter expense number: "))
    expense = expenses[choice - 1]
    print("What do you want to edit?")
    print("1. Title")
    print("2. Amount")
    print("3. Category")
    print("4. Everything")

    edit_choice = int(input("Enter your choice: "))

    if edit_choice == 1:
        expense.title = input("New title: ")
    elif edit_choice == 2:
            expense.amount = float(input("New amount: "))
    elif edit_choice == 3:
            expense.category = input("New category: ")
    elif edit_choice == 4:
           expense.title = input("New title: ")
           expense.amount = float(input("New amount: "))
           expense.category = input("New category: ")
    else:
        print("Invalid choice!")
    save_expenses(expenses)
    print("Expense Updated Successfully!")