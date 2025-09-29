import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("file:///path/to/LAB04/index.html")  # chỉnh lại đường dẫn đúng của bạn
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    assert "Đăng nhập thành công" in driver.page_source
    driver.quit()

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get("file:///path/to/LAB04/index.html")
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    assert "không đúng" in driver.page_source
    driver.quit()

def test_login_empty():
    driver = webdriver.Chrome()
    driver.get("file:///path/to/LAB04/index.html")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    assert "Vui lòng nhập đầy đủ" in driver.page_source
    driver.quit()
