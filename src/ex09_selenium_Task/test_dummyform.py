import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dummyform():
    chromeoption = webdriver.ChromeOptions()
    chromeoption.add_argument("--incognito")
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(2)
    username = driver.find_element(By.NAME,'email')
    username.send_keys("test1501@gmail.com")

    time.sleep(2)
    password = driver.find_element(By.NAME,'Password')
    password.send_keys("Test@1234")

    time.sleep(2)
    company = driver.find_element(By.NAME,'company')
    company.send_keys("Toshal Infotech")

    time.sleep(2)
    mb_n = driver.find_element(By.NAME,"mobile number")
    mb_n.send_keys("124658900")

    time.sleep(2)
    country = driver.find_element(By.XPATH,"//div/label[contains(text(),'Country')]/input")
    country.send_keys("INDIA")

    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Submit')]").click()

    print("Test Case Pased")
    time.sleep(10)






