import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def test_navigate_to_login_page(setup_driver):
    driver = setup_driver
    
    # Open the Website
    driver.get("https://practicetestautomation.com/")
    
    # Click on Practice
    practice = driver.find_element(By.XPATH, "//a[normalize-space()='Practice']")
    practice.click()
    
    # Click on Test Login Page
    test_login_page = driver.find_element(By.XPATH, "//a[normalize-space()='Test Login Page']")
    test_login_page.click()
    
    # Let us verify that we are on the right URL
    assert ("https://practicetestautomation.com/practice-test-login/") in driver.current_url
    
# NOW, Let's automate the web elements
def test_login_page(setup_driver):
    driver = setup_driver
    
    # Open the Website
    driver.get(" https://practicetestautomation.com/practice-test-login/")
    
    # Enter Username and Password
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()
    
    # Let us verify that we are on the right URL
    assert ("https://practicetestautomation.com/logged-in-successfully/") in driver.current_url
    
    # Verify the page contains the success text
    page_text = driver.page_source
    assert "Congratulations" in page_text or "successfully logged in" in page_text
    
    # Let's verifiy the presence of the log out button
    assert driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").is_displayed()
    

def test_negative_username(setup_driver):
    driver = setup_driver
    
    # Open the Website
    driver.get(" https://practicetestautomation.com/practice-test-login/")
    
    # Enter Username and Password
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("incorrectUser")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()
    
    error_message = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error_message
    

def test_negative_password(setup_driver):
    driver = setup_driver
    
    # Open the Website
    driver.get(" https://practicetestautomation.com/practice-test-login/")
    
    # Enter Username and Password
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("incorrectPassword")
    
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()
    
    error_message = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error_message
    
    