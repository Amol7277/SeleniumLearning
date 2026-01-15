import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_Payment():
    chrome_options = Options()
    # chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()

    driver.get("https://selectorshub.com/xpath-practice-page/")

    # cardName = driver.find_element(By.XPATH, "//h6[contains(text(),'Payment Page')]")
    scroll = driver.find_element(By.XPATH, "//h6[contains(text(),'Payment Page')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", scroll)

    time.sleep(3)
    cardName = driver.find_element(By.ID, "cardName")
    cardName.send_keys("Test Visa")

    time.sleep(2)
    cardNumber = driver.find_element(By.ID,"cardNumber")
    cardNumber.send_keys("4111111111111111")

    time.sleep(2)
    expiry = driver.find_element(By.ID,"expiry")
    expiry.send_keys("0526")

    time.sleep(2)
    cvv = driver.find_element(By.ID,"cvv")
    cvv.send_keys("123")

    time.sleep(2)
    submit = driver.find_element(By.XPATH,"//button[@type='submit']")
    submit.click()

    print("Test Case Pased")
    time.sleep(10)





