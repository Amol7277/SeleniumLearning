import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_svg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    state_list = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in state_list:
        state.get_attribute("aria-label")
        print(state.get_attribute("aria-label"))
        if "Maharashtra  " in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(10)