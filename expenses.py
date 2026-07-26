class Expense:
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
    def __str__(self):
        return(
            f"Title     : {self.title}\n"
            f"Amount    : $ {self.amount}\n"
            f"Category  : {self.category}\n"
            f"Date      : {self.date}"
        )
