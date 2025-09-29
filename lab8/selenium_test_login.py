import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    opts = Options()
    driver = webdriver.Chrome(options=opts)
    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/form_login.html")
    driver.set_window_size(1200, 900)
    yield driver
    driver.quit()

def wait_for_message_text(driver, timeout=3):
    wait = WebDriverWait(driver, timeout)
    try:
        wait.until(lambda d: d.find_element(By.ID, "message").text.strip() != "")
    except TimeoutException:
        pass
    return driver.find_element(By.ID, "message").text.strip()

def test_login_success(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = wait_for_message_text(driver, timeout=3)
    assert "Đăng nhập thành công" in message

def test_login_wrong_password(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrong123")
    driver.find_element(By.CSS_SELECTOR, ".btn.primary").click()

    message = wait_for_message_text(driver, timeout=3)
    assert "Tên người dùng hoặc Mật khẩu không đúng" in message

def test_login_empty_input(driver):
    driver.refresh()
    WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    time.sleep(0.3)
    message = wait_for_message_text(driver)
    assert "Vui lòng nhập đầy đủ Tên người dùng và Mật khẩu." in message
