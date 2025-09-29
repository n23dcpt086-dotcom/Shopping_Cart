import pytest
from atm_module import ATM

@pytest.fixture
def atm():
    return ATM(pin="1234", balance=1_000_000)

def test_verify_pin_correct(atm):
    assert atm.verify_pin("1234") is True

def test_verify_pin_incorrect(atm):
    assert atm.verify_pin("9999") is False

def test_withdraw_success(atm):
    result = atm.withdraw("1234", 200_000)
    assert "✅ Rút" in result
    assert atm.balance == 800_000

def test_withdraw_invalid_pin(atm):
    result = atm.withdraw("0000", 200_000)
    assert result == "❌ PIN không hợp lệ"

def test_withdraw_invalid_amount(atm):
    result = atm.withdraw("1234", -100)
    assert result == "❌ Số tiền phải > 0"

def test_withdraw_insufficient_funds(atm):
    result = atm.withdraw("1234", 2_000_000)
    assert "❌ Số dư không đủ" in result
