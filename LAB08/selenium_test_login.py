import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8000/LAB04/LAB04.HTML") 
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text

    assert "Đăng nhập thành công" in message

def test_login_fail(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("sai_mat_khau")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text

    assert "Tên người dùng hoặc Mật khẩu không đúng" in message

def test_login_empty(driver):
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text

    assert "Vui lòng nhập tên đăng nhập và mật khẩu" in message

