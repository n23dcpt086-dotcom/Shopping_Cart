import hashlib
import pytest
from unittest.mock import MagicMock
import withdraw_module

CARD = "1234567890123456"
CORRECT_PIN = "1234"
CORRECT_PIN_HASH = hashlib.sha256(CORRECT_PIN.encode()).hexdigest()

def make_mock_conn(fetchone_values):
    mock_cur = MagicMock()
    mock_cur.fetchone.side_effect = list(fetchone_values)
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cur
    mock_conn.is_connected.return_value = True
    return mock_conn

def test_verify_pin_correct(monkeypatch):
    mock_conn = make_mock_conn([(CORRECT_PIN_HASH,)])
    monkeypatch.setattr(withdraw_module, "get_db_connection", lambda: mock_conn)
    assert withdraw_module.verify_pin(CARD, CORRECT_PIN) is True

def test_verify_pin_wrong(monkeypatch):
    mock_conn = make_mock_conn([("otherhash",)])
    monkeypatch.setattr(withdraw_module, "get_db_connection", lambda: mock_conn)
    assert withdraw_module.verify_pin(CARD, "9999") is False

def test_withdraw_success(monkeypatch):
    account_info = (1, 1_000_000)
    mock_conn = make_mock_conn([account_info])
    monkeypatch.setattr(withdraw_module, "get_db_connection", lambda: mock_conn)
    result = withdraw_module.withdraw(CARD, 500_000)
    assert result is True
    assert mock_conn.commit.called

def test_withdraw_insufficient(monkeypatch):
    account_info = (1, 1000)
    mock_conn = make_mock_conn([account_info])
    monkeypatch.setattr(withdraw_module, "get_db_connection", lambda: mock_conn)
    result = withdraw_module.withdraw(CARD, 2_000_000)
    assert result is False
    assert mock_conn.rollback.called

def test_withdraw_invalid_amount(monkeypatch):
    mock_conn = make_mock_conn([])
    monkeypatch.setattr(withdraw_module, "get_db_connection", lambda: mock_conn)
    result = withdraw_module.withdraw(CARD, 0)
    assert result is False
