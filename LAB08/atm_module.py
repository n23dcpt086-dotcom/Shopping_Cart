class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")
        if amount > self.balance:
            raise Exception("Không đủ tiền trong tài khoản")
        self.balance -= amount
        return self.balance
