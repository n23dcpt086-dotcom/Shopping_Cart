import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  
import pytest
from atm_module import verify_pin, withdraw

def test_verify_pin_correct():
    atm = ATM(1000, "1234")
    assert atm.verify_pin("1234") == True

def test_verify_pin_wrong():
    atm = ATM(1000, "1234")
    assert atm.verify_pin("0000") == False

def test_withdraw_success():
    atm = ATM(1000, "1234")
    assert atm.withdraw(200) == 800

def test_withdraw_insufficient_funds():
    atm = ATM(1000, "1234")
    with pytest.raises(Exception, match="Không đủ tiền"):
        atm.withdraw(2000)

def test_withdraw_invalid_amount():
    atm = ATM(1000, "1234")
    with pytest.raises(ValueError, match="Số tiền rút phải > 0"):
        atm.withdraw(0)
