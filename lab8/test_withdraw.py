import pytest
from atm_module import verify_pin, withdraw

# ---- TEST verify_pin ----
def test_verify_pin_correct():
    assert verify_pin("1234", "1234") == True

def test_verify_pin_incorrect():
    assert verify_pin("1111", "1234") == False

# ---- TEST withdraw ----
def test_withdraw_success():
    assert withdraw(1000, 200) == 800

def test_withdraw_insufficient():
    assert withdraw(500, 1000) == "Insufficient funds"

def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(500, 0)
