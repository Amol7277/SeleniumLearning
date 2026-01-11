import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@allure.title("exception_handle")
@allure.description("Verify exception_handle")
def test_NoSuchElementException():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver,timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    try:
        popup = driver.find_element(By.XPATH, "//span[@data-cy='closeModal_TestException']")
        popup.click()
    except NoSuchElementException as nse:
        print(nse.msg)