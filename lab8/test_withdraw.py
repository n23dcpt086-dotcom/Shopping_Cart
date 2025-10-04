import pytest
from atm_module import ATM

def test_verify_pin_correct():
    atm = ATM("1234", 1000)
    assert atm.verify_pin("1234") is True

def test_verify_pin_incorrect():
    atm = ATM("1234", 1000)
    assert atm.verify_pin("0000") is False

def test_withdraw_success():
    atm = ATM("1234", 1000)
    result = atm.withdraw("1234", 500)
    assert "success" in result
    assert atm.balance == 500

def test_withdraw_insufficient_funds():
    atm = ATM("1234", 100)
    result = atm.withdraw("1234", 200)
    assert result == "Insufficient funds"

def test_withdraw_invalid_pin():
    atm = ATM("1234", 1000)
    result = atm.withdraw("0000", 100)
    assert result == "Invalid PIN"

def test_withdraw_invalid_amount():
    atm = ATM("1234", 1000)
    result = atm.withdraw("1234", -50)
    assert result == "Invalid amount"
