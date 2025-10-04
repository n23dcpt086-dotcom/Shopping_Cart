# selenium_test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LOGIN_PAGE = "file:///C:/Users/ADMIN/Shopping_Cart/labs/lab08-testing/login_form.html"


def test_login_success():
    driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CLASS_NAME, "login-btn")

    username.send_keys("admin123")
    password.send_keys("password123")
    login_btn.click()

    time.sleep(1)
    alert = driver.switch_to.alert
    assert "Đăng nhập thành công" in alert.text
    alert.accept()
    driver.quit()


def test_login_fail():
    driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CLASS_NAME, "login-btn")

    username.send_keys("abc")  # username < 5 ký tự
    password.send_keys("123")  # password < 8 ký tự
    login_btn.click()

    time.sleep(1)
    username_error = driver.find_element(By.ID, "usernameError").text
    password_error = driver.find_element(By.ID, "passwordError").text

    assert "ít nhất 5 ký tự" in username_error
    assert "ít nhất 8 ký tự" in password_error
    driver.quit()


def test_login_empty():
    driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE)

    login_btn = driver.find_element(By.CLASS_NAME, "login-btn")
    login_btn.click()

    time.sleep(1)
    username_error = driver.find_element(By.ID, "usernameError").text
    password_error = driver.find_element(By.ID, "passwordError").text

    assert "không được để trống" in username_error
    assert "không được để trống" in password_error
    driver.quit()
