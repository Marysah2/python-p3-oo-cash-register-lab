class CashRegister:
    def __init__(self, discount=0):  # default discount is 0
        self.total = 0.0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        # remove last transaction items from the list
        count = 0
        total_price = 0.0
        while total_price < self.last_transaction_amount and self.items:
            self.items.pop()
            count += 1
            total_price = count * (self.last_transaction_amount / count)  # approximate
        self.last_transaction_amount = 0.0
