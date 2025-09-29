import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

HTML_PATH = "file:///C:/Users/ADMIN/Shopping_Cart/LAB04/index.html"

@pytest.fixture(scope="module")
def driver():
    drv = webdriver.Chrome()
    drv.get(HTML_PATH)
    yield drv
    drv.quit()

def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert "Đăng nhập thành công" in msg

def test_login_fail(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert "không đúng" in msg

def test_login_empty(driver):
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert "Vui lòng nhập" in msg
