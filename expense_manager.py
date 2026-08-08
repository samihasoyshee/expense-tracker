from file_handler import save_expenses
from expenses import Expense
from datetime import datetime
def add_expense(expenses):
    title = input("Which item did you buy?:")
    amount = input("How much did it cost?: ")
    category = input("What category it belongs to?: ")
    date = datetime.now().strftime("%d-%m-%Y")

    expense = Expense(title,
                        amount,
                        category,
                        date)
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

    print(f"Total Expense: ${total}")

    print("\n===Expenses by Category===")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount}")

def edit_expense(expenses):
    view_expenses(expenses)

    choice = int(input("Enter expense number: "))
    if choice < 1 or choice > len(expenses):
        print("Invalid expense number!")
        return
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

def statistic(expenses):
    print("-----Expense Statistics-----")
    total_expenses = len(expenses)
    print(f"Total Expense: ${total_expenses}")

    if not expenses:
        print("You spent $0")
    else:
        total_spent = 0
        total_spent = sum(expense.amount for expense in expenses)
    print(f'\nTotal Amount Spent: ${total_spent: .2f}')

    if total_spent>0:
        average = total_spent/ total_expenses
    else: 
        average = 0
    print(f"Average Expense: ${average:.2f}")

    if expenses:
        highest = max(expenses, key= lambda expense:expense.amount)
        lowest= min(expenses, key = lambda  expense: expense.amount)

        print(f"\nHighest Expense:{highest.title} - ${highest.amount:.2f}")
        print(f"Lowest Expense:{lowest.title} - ${lowest.amount:.2f}")

        category_totals = {}
        for expense in expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount

        print("\nExpense by category:\n")
        for category, amount in category_totals.items():
            print(f"{category} : ${amount:.2f}")

def sort_expenses(expenses):

        print("\n----Sort Expense----")
        print("1. Sort by Title")
        print("2. Sort by Amount")
        print("3. Sort by Date")
        print("4. Sort by Category")

        choice =input("Enter your choice: ")

        if choice == "1":
            sorted_expense = sorted(expenses, key=lambda expense: expense.title)
            for expense in sorted_expense:
                print(expense)
        elif choice == "2":
            sorted_expense = sorted(expenses, key=lambda expense: expense.amount)
            for expense in sorted_expense:
                print(expense)
        elif choice == "3":
            sorted_expense = sorted(expenses, key=lambda expense: expense.date)
            for expense in sorted_expense:
                print(expense)
        elif choice == "4":
            sorted_expense = sorted(expenses, key=lambda expense: expense.category)
            for expense in sorted_expense:
                print(expense)

                    

            

