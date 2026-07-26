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
        