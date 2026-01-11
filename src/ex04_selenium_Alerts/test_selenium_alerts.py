import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_JS_Aert():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(1)

    JSalert = driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Alert')]")
    JSalert.click()

    # WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located())
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(1)
    result = driver.find_element(By.ID,'result')
    assert  result.text == "You successfully clicked an alert"


def test_JS_Confirm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(1)

    JSalert = driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Confirm')]")
    JSalert.click()

    # WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located())
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(1)
    result = driver.find_element(By.ID,'result')
    assert  result.text == "You clicked: Ok"

def test_JS_Prompt():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(1)

    JSalert = driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Prompt')]")
    JSalert.click()

    # WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located())
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.send_keys("Test Alert")
    time.sleep(5)
    alert.accept()

    time.sleep(1)
    result = driver.find_element(By.ID,'result')
    assert  result.text == "You entered: Test Alert"


