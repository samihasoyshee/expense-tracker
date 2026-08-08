class Expense:
    def __init__(self, title, amount, category, date):
        self.title = title.title()
        self.amount = float(amount)
        self.category = category.title()
        self.date = date
    def __str__(self):
        return f"{self.title} | ${self.amount} | {self.category} | {self.date}"
        
    def to_dict(self):
        return {
            "title" : self.title,
            "amount": self.amount,
            "category": self.category,
            "date" : self.date
        }
