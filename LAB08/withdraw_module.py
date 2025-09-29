import mysql.connector
import hashlib

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="atm"
    )

def verify_pin(card_no, pin):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pin_hash FROM accounts WHERE card_no=%s", (card_no,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        return pin_hash == result[0]
    return False

def withdraw(card_no, amount):
    if amount <= 0:
        return False
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT account_id, balance FROM accounts WHERE card_no=%s FOR UPDATE", (card_no,))
        account = cursor.fetchone()
        if not account:
            return False
        account_id, balance = account
        if balance < amount:
            conn.rollback()
            return False
        new_balance = balance - amount
        cursor.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (new_balance, account_id))
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s,%s,%s)", (account_id, 'withdraw', amount))
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()
