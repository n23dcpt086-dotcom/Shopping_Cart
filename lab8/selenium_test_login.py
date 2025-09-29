import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://github.com/n23dcpt086-dotcom/Shopping_Cart/blob/774838f60e0d835d42833f275208e089a2751c22/LAB04/form_login.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver, username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button.primary").click()
    time.sleep(1)  # chờ JS xử lý

    message = driver.find_element(By.ID, "message").text
    return message

def test_login_success(driver):
    msg = login(driver, "admin", "admin123")
    assert "Đăng nhập thành công" in msg

def test_login_fail(driver):
    msg = login(driver, "admin", "123456")
    assert msg == "Tên người dùng hoặc Mật khẩu không đúng."

def test_login_empty(driver):
    msg = login(driver, "", "")
    assert msg == "Vui lòng nhập đầy đủ Tên người dùng và Mật khẩu."
