def verify_pin(input_pin: str, real_pin: str) -> bool:
    """Trả về True nếu PIN khớp, False nếu không."""
    return input_pin == real_pin

def withdraw(balance: float, amount: float):
    """
    Mô phỏng rút tiền.
    - Nếu amount <= 0 => ValueError
    - Nếu amount > balance => trả về "Insufficient funds"
    - Ngược lại => trả về số dư mới
    """
    if amount <= 0:
        raise ValueError("Số tiền rút phải lớn hơn 0")
    if amount > balance:
        return "Insufficient funds"
    return balance - amount
