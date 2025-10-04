def verify_pin(input_pin, real_pin):
    """Hàm kiểm tra mã PIN"""
    return input_pin == real_pin


def withdraw(balance, amount):
    """Hàm mô phỏng rút tiền"""
    if amount <= 0:
        raise ValueError("Số tiền rút phải lớn hơn 0")
    if amount > balance:
        return "Insufficient funds"
    return balance - amount
