import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_PAGE = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "../LAB04/form_login.html"))

@pytest.fixture
def driver():
    try:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except Exception:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()

def click_login_button(driver):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-btn"))
    ).click()

def test_login_success(driver):
    driver.get(LOGIN_PAGE)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("admin123")
    driver.find_element(By.ID, "password").send_keys("password123")
    click_login_button(driver)

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Đăng nhập thành công" in alert.text
    alert.accept()

def test_login_validation_fail(driver):
    driver.get(LOGIN_PAGE)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "username").send_keys("abc")   # <5 ký tự
    driver.find_element(By.ID, "password").send_keys("123")   # <8 ký tự
    click_login_button(driver)

    WebDriverWait(driver, 3).until(
        lambda d: d.find_element(By.ID, "usernameError").text.strip() != "" or
                  d.find_element(By.ID, "passwordError").text.strip() != ""
    )
    u_err = driver.find_element(By.ID, "usernameError").text.strip()
    p_err = driver.find_element(By.ID, "passwordError").text.strip()
    assert u_err != "" and ("ít nhất 5" in u_err or "không được để trống" in u_err)
    assert p_err != "" and ("ít nhất 8" in p_err or "không được để trống" in p_err)

def test_login_empty_input(driver):
    driver.get(LOGIN_PAGE)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    driver.execute_script("document.getElementById('username').removeAttribute('required')")
    driver.execute_script("document.getElementById('password').removeAttribute('required')")

    click_login_button(driver)

    WebDriverWait(driver, 3).until(
        lambda d: d.find_element(By.ID, "usernameError").text.strip() != "" and
                  d.find_element(By.ID, "passwordError").text.strip() != ""
    )
    assert "không được để trống" in driver.find_element(By.ID, "usernameError").text
    assert "không được để trống" in driver.find_element(By.ID, "passwordError").text
