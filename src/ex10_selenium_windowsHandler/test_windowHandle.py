import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_windowHandle():
    chrome_option = Options()
    chrome_option.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_option)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    driver.find_element(By.LINK_TEXT,"Click Here").click()

    driver.switch_to.window(driver.window_handles[1])
    print(driver.window_handles[1])
    time.sleep(2)
    # print(driver.page_source)
    assert "New Window" in driver.page_source
    print("Test 1 Passed")

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # print(driver.page_source)
    assert "Opening a new window" in driver.page_source
    print("Test 2 Passed")

    time.sleep(5)

