class ATM:
    def __init__(self, pin="1234", balance=1_000_000):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def withdraw(self, input_pin, amount):
        if not self.verify_pin(input_pin):
            return "❌ PIN không hợp lệ"
        if amount <= 0:
            return "❌ Số tiền phải > 0"
        if amount > self.balance:
            return f"❌ Số dư không đủ. Hiện tại: {self.balance:,} VND"
        self.balance -= amount
        return f"✅ Rút {amount:,} VND thành công. Số dư còn lại: {self.balance:,} VND"
