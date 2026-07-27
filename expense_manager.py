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

 
        
