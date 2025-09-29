import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/LAB04.html")
    yield driver
    driver.quit()


def test_login_success(browser):
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, ".btn.primary")

    username.clear()
    password.clear()
    username.send_keys("admin")
    password.send_keys("admin123")
    login_button.click()

    time.sleep(1)  
    message = browser.find_element(By.ID, "message").text
    assert "Đăng nhập thành công" in message


def test_login_wrong(browser):
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, ".btn.primary")

    username.clear()
    password.clear()
    username.send_keys("wronguser")
    password.send_keys("123456")
    login_button.click()

    time.sleep(1)
    message = browser.find_element(By.ID, "message").text
    assert "không đúng" in message


def test_login_empty(browser):
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, ".btn.primary")

    username.clear()
    password.clear()
    login_button.click()

    time.sleep(1)
    message = browser.find_element(By.ID, "message").text
    assert "Vui lòng nhập đầy đủ" in message
