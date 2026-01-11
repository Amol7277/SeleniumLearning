import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

def test_staticDropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown = driver.find_element(By.ID, 'dropdown')
    # actionChains = ActionChains(driver)
    select = Select(dropdown)
    select.select_by_index(2)
    print("selected_by_index")

    time.sleep(5)

    select.select_by_value("1")
    print("selected_by_value")

    time.sleep(5)

    select.select_by_visible_text("Option 2")
    print("selected_by_visible_text")

    time.sleep(10)

