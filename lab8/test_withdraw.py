import pytest
from atm_module import verify_pin, withdraw

def test_verify_pin_correct():
    assert verify_pin("1234", "1234") is True

def test_verify_pin_incorrect():
    assert verify_pin("0000", "1234") is False

def test_withdraw_success():
    assert withdraw(1000, 200) == 800

def test_withdraw_insufficient():
    assert withdraw(50, 100) == "Insufficient funds"

def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(500, 0)
