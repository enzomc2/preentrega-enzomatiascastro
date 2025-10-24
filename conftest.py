import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import login

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(2)
    yield driver
    time.sleep(3)
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver