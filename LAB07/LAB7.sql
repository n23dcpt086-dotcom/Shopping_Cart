-- 1. Tạo Database
CREATE DATABASE atm_demo;
USE atm_demo;

-- 2. Tạo Bảng Accounts (Lưu số dư)
CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_holder_name VARCHAR(100) NOT NULL,
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00
);

-- 3. Tạo Bảng Cards (Lưu số thẻ và PIN đã hash)
CREATE TABLE cards (
    card_no VARCHAR(16) PRIMARY KEY,
    account_id INT NOT NULL,
    pin_hash CHAR(64) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- 4. Tạo Bảng Transactions (Ghi nhật ký giao dịch)
CREATE TABLE transactions (
    tx_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    card_no VARCHAR(16) NOT NULL,
    atm_id INT NOT NULL,
    tx_type VARCHAR(20) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    tx_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO accounts (account_holder_name, balance) VALUES ('Nguyen Van A', 5000000.00); 
INSERT INTO cards (card_no, account_id, pin_hash) VALUES ('1234567890123456', 1, '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');