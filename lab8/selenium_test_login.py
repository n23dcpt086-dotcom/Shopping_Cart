import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/LAB04.html")
    yield driver
    driver.quit()


def test_login_success(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert "Đăng nhập thành công" in message


def test_login_wrong_password(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert "không đúng" in message


def test_login_empty_input(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert "Vui lòng nhập đầy đủ" in message
