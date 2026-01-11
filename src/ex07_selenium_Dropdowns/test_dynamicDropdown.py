import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Dynamic Dropdown of MakeMyTrip")
@allure.description("Dynamic Dropdown of MakeMyTrip")
def test_Dynamic_Dropdown():

    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    popup = driver.find_element(By.XPATH,"//span[@data-cy='closeModal']")
    popup.click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//img[@alt='minimize']").click()

    time.sleep(2)

    # driver.find_element(By.ID,"root").click()
    # time.sleep(2)
    # fromcity = driver.find_element(By.XPATH, "//label[@for='fromCity']")
    # fromcity = driver.find_element(By.ID,"fromCity")

    SelectFromCity = driver.find_element(By.ID,"fromCity")
    SelectToCity = driver.find_element(By.ID,"toCity")

    actionChain= ActionChains(driver)

    time.sleep(2)
    actionChain.move_to_element(SelectFromCity).double_click().send_keys_to_element(SelectFromCity,"STV").perform()

    time.sleep(2)
    actionChain.move_to_element(SelectFromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(2)
    actionChain.move_to_element(SelectToCity).double_click().send_keys_to_element(SelectToCity,"BOM").perform()

    time.sleep(2)
    actionChain.move_to_element(SelectFromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(10)

