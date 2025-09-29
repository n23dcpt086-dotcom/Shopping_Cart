import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/form_login.html")
    yield driver
    driver.quit()

def get_message(driver):
    return driver.find_element(By.ID, "message").text

def test_login_success(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = get_message(driver)
    assert "Đăng nhập thành công" in message

def test_login_wrong_password(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = get_message(driver)
    assert "Tên người dùng hoặc Mật khẩu không đúng." in message

def test_login_empty_input(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = get_message(driver)
    assert "Vui lòng nhập đầy đủ Tên người dùng và Mật khẩu." in message
