class ATM:
    def __init__(self, pin: str, balance: int):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, input_pin: str) -> bool:
        """Kiểm tra PIN nhập vào"""
        return self.pin == input_pin

    def withdraw(self, input_pin: str, amount: int) -> str:
        """Rút tiền khi PIN đúng và số dư đủ"""
        if not self.verify_pin(input_pin):
            return "Invalid PIN"
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdraw {amount} success, balance {self.balance}"
