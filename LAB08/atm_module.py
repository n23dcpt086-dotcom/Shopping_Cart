class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def withdraw(self, input_pin, amount):
        if not self.verify_pin(input_pin):
            return "Invalid PIN"
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdraw successful"
