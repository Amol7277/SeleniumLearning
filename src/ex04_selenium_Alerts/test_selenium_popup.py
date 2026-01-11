import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium_popup():

    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    popup = driver.find_element(By.XPATH,"//span[@data-cy='closeModal']")
    popup.click()


    action = ActionChains(driver=driver)
    
    time.sleep(5)


