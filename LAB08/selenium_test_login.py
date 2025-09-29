import time
from selenium import webdriver
from selenium.webdriver.common.by import By

HTML_PATH = "file:///absolute/path/to/Shopping_Cart/LAB04/index.html"  

def test_login_success():
    driver = webdriver.Chrome()
    driver.get(HTML_PATH)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    assert "Đăng nhập thành công" in driver.page_source
    driver.quit()

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get(HTML_PATH)
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    assert "không đúng" in driver.page_source
    driver.quit()

def test_login_empty():
    driver = webdriver.Chrome()
    driver.get(HTML_PATH)
    driver.find_element(By.CLASS_NAME, "primary").click()
    time.sleep(1)
    assert "Vui lòng nhập đầy đủ" in driver.page_source
    driver.quit()
