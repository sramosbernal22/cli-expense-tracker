class Expense:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        # __repr__ should return an unambiguous string for developers,
        # ideally one that can be used to recreate the object.
        return (
            f"Expense(description={self.description!r}, amount={self.amount!r}, "
            f"category={self.category!r}, date={self.date!r})"
        )

    def __str__(self):
        # __str__ should return a clean, user-friendly string for printing.
        return (
            f"{self.date}: {self.description} - {self.category} "
            f"(${self.amount})"
        )
