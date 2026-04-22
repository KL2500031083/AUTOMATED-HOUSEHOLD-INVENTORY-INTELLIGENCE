from datetime import datetime

class Item:
    def __init__(self, name, quantity, expiry):
        self.name = name
        self.quantity = int(quantity)
        self.expiry = expiry  # YYYY-MM-DD

    def is_expired(self):
        today = datetime.today().date()
        expiry_date = datetime.strptime(self.expiry, "%Y-%m-%d").date()
        return expiry_date <= today

    def __str__(self):
        return f"{self.name} | Qty: {self.quantity} | Expiry: {self.expiry}"