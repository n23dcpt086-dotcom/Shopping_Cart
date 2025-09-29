import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/form_login.html")
    yield driver
    driver.quit()

def get_message(driver):
    time.sleep(1)  
    return driver.find_element(By.ID, "message").text.strip()

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
    assert "không đúng" in message

def test_login_empty_input(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = get_message(driver)
    assert "Vui lòng nhập đầy đủ" in message
