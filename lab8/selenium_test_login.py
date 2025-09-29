import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ADMIN/Shopping_Cart/LAB04/LAB04.html")  
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    assert "Welcome" in driver.page_source

def test_login_wrong_password(driver):
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("wrong")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    assert "Invalid" in driver.page_source

def test_login_empty_input(driver):
    driver.find_element(By.NAME, "username").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    assert "Please enter" in driver.page_source
