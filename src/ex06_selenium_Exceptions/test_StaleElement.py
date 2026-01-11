import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

@allure.title("stale_element")
@allure.description("stale_element")
def test_StaleElementException():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver= driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    # popup = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    # driver.refresh()
    # popup.click()

    try:
        popup = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
        driver.refresh()
        popup.click()

    except StaleElementReferenceException as SE:
        print("Error Message is=> ",SE.msg)
