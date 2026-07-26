from expenses import Expense
from expense_manager import add_expense, view_expenses,search_expense
from datetime import datetime

expenses = [ ]


def main():
    print("=-=" * 7)
    print("  EXPENSE TRACKER")
    print("=-=" * 7)
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Statistics")
    print("5. Sort Expenses")
    print("6. Edit Expense")
    print("7. Delete Expense")
    print("8. Save")
    print("9. Exit")

while True:
    main()
    choice = input("\nChoose an option: ")
    if choice == "1":
        title = input("Which item did you buy?:")
        amount = input("How much did it cost?: ")
        category = input("What category it belongs to?: ")
        date = datetime.now().strftime("%d-%m-%Y")

        expense = Expense(title,
                          amount,
                          category,
                          date)
        add_expense(expenses, expense)
        input("\nPress Enter to continue...")
        
    elif choice == "2":
        view_expenses(expenses)
        input("\nPress Enter to continue...")

    elif choice == "3":
        keyword = input("Enter a title to search: ")
        search_expense(expenses, keyword)
        input("\nPress Enter to continue...")
        


