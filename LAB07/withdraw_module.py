import mysql.connector
import hashlib
from mysql.connector import Error

# Cấu hình kết nối DB
DB_CONFIG = {
    "user": "root",
    "password": "Thanhvan1510!" ,
    "database": "atm_demo"
}

# (Phần còn lại của hàm get_db_connection, verify_pin, và withdraw giữ nguyên)
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"❌ Lỗi kết nối MySQL: Vui lòng kiểm tra Server và thông tin đăng nhập! Lỗi: {e}")
        return None

def verify_pin(card_no, pin):
    conn = get_db_connection()
    if not conn: return False
    cur = conn.cursor()
    try:
        cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
        row = cur.fetchone()
        if not row: return False
        db_pin_hash = row[0]
        input_pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        return db_pin_hash == input_pin_hash
    except Error as e:
        print(f"Lỗi DB trong verify_pin: {e}"); return False
    finally:
        if conn and conn.is_connected(): cur.close(); conn.close()

def withdraw(card_no, amount):
    if amount <= 0: print("Lỗi: Số tiền rút phải lớn hơn 0."); return False
    conn = get_db_connection()
    if not conn: return False
    cur = conn.cursor()
    
    try:
        conn.start_transaction() 
        cur.execute("""
            SELECT a.account_id, a.balance FROM accounts a 
            JOIN cards c ON a.account_id = c.account_id WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        
        account_info = cur.fetchone()
        if not account_info: raise Exception("Thẻ không hợp lệ.")
        account_id, current_balance = account_info

        if current_balance < amount:
            raise Exception(f"Số dư không đủ. Số dư hiện tại: {current_balance:,.0f} VND")
            
        new_balance = current_balance - amount
        
        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s", (amount, account_id))
        
        cur.execute(
            "INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after) VALUES(%s, %s, 1, 'WITHDRAW', %s, %s)",
            (account_id, card_no, amount, new_balance)
        )
        
        conn.commit()
        print(f"\n✅ RÚT TIỀN THÀNH CÔNG! Số tiền rút: {amount:,.0f} VND. Số dư mới: {new_balance:,.0f} VND")
        return True

    except Exception as e:
        conn.rollback()
        print(f"\n❌ LỖI GIAO DỊCH: {e}")
        return False
        
    finally:
        if conn and conn.is_connected(): cur.close(); conn.close()

# --- Phần chạy Test Tự động ---
if __name__ == "__main__":
    CARD_NO_DEMO = '1234567890123456'
    PIN_CORRECT = '1234'
    AMOUNT_SUCCESS = 500000  # 500k
    AMOUNT_FAIL_FUNDS = 6000000 # 6 triệu (sẽ gây lỗi)
    
    print("=========================================")
    print("       DEMO MODULE RÚT TIỀN (LAB 07)     ")
    print("=========================================")
    
    print("\n--- 1. TEST PIN SAI ---")
    if not verify_pin(CARD_NO_DEMO, '4321'): print("✅ Xác thực PIN SAI: Thất bại như dự kiến.")
        
    print("\n--- 2. TEST RÚT TIỀN THÀNH CÔNG (Rút 500k) ---")
    if verify_pin(CARD_NO_DEMO, PIN_CORRECT): withdraw(CARD_NO_DEMO, AMOUNT_SUCCESS)
    
    print("\n--- 3. TEST KHÔNG ĐỦ SỐ DƯ (Yêu cầu 6M) ---")
    if verify_pin(CARD_NO_DEMO, PIN_CORRECT): withdraw(CARD_NO_DEMO, AMOUNT_FAIL_FUNDS)