from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
import time


@pytest.fixture(scope="function")
def get_browser():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/login/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(5)
    yield driver
    time.sleep(15)
    driver.quit()