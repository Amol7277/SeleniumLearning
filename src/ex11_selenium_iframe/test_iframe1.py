import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_iframeHandle():
    chrome_option = Options()
    chrome_option.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_option)
    driver.maximize_window()
    driver.get("https://selectorshub.com/iframe-scenario/")

    frame1 = driver.find_element(By.ID,"pact1")
    time.sleep(2)
    driver.switch_to.frame(frame1)

    time.sleep(2)
    crush1 = driver.find_element(By.ID,"inp_val")
    crush1.send_keys("test")

    frame2 = driver.find_element(By.ID,"pact2")
    time.sleep(2)
    driver.switch_to.frame(frame2)

    time.sleep(2)
    current_crush1 = driver.find_element(By.ID,"jex")
    current_crush1.send_keys("test")

    frame3 = driver.find_element(By.ID,"pact3")
    time.sleep(2)
    driver.switch_to.frame(frame3)

    time.sleep(2)
    Destiny = driver.find_element(By.ID,"glaf")
    Destiny.send_keys("test")

    time.sleep(2)
    driver.switch_to.default_content()
    driver.switch_to.frame(frame1)

    # driver.switch_to.parent_frame()
    # driver.switch_to.parent_frame()

    time.sleep(2)
    crush1.clear()
    crush1.send_keys("testAmol")

    time.sleep(5)