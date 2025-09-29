import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/form_login.html")
    yield driver
    driver.quit()


def wait_for_message_text(driver, timeout=3):
    """Đợi message hiển thị rồi lấy text"""
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    return element.text.strip()


def test_login_success(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = wait_for_message_text(driver)
    assert "Đăng nhập thành công" in message


def test_login_wrong_password(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = wait_for_message_text(driver)
    assert "Tên người dùng hoặc Mật khẩu không đúng" in message


def test_login_empty_input(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = wait_for_message_text(driver)
    expected = "Vui lòng nhập đầy đủ Tên người dùng và Mật khẩu."
    assert message.startswith(expected)
