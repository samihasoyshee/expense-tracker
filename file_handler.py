import json   
from expenses import Expense
def save_expenses(expenses):
    expense_data =[
        expense.to_dict()
        for expense in expenses]
    with open("expenses.json","w") as file:
        json.dump(expense_data, file, indent =4)

def load_expenses():
    expenses = []
    with open("expenses.json","r") as file:
        expense_data = json.load(file)
        for data in expense_data:
            expense = Expense(
                data["title"],
                data["amount"],
                data["category"],
                data["date"]
            )
            expenses.append(expense)
        return expenses