import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.script_key import ScriptKey
from selenium.webdriver.common.keys import Keys

@allure.title("Dynamic Dropdown of SpiceJet")
@allure.description("Dynamic Dropdown of SpiceJet")
def test_dynamicDropdown2():
    driver=webdriver.Chrome()
    driver.maximize_window()
    # driver.get("https://google.com")
    # dd = driver.find_element(By.NAME,'q')
    # time.sleep(2)
    # action = ActionChains(driver=driver)
    # time.sleep(2)
    # action.move_to_element(dd).send_keys_to_element(dd,"spicejet").perform()
    # time.sleep(2)
    # action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    #
    # print("Test Passed")


    driver.get("https://spicejet.com/")

    time.sleep(10)

    fromCity= driver.find_element(By.XPATH,"//div[@data-testid='to-testID-origin']")
    ToCity= driver.find_element(By.XPATH,"//div[@data-testid='to-testID-destination']")

    action = ActionChains(driver)
    action.move_to_element(fromCity).click().send_keys_to_element(fromCity,"STV").perform()

    time.sleep(2)

    action.move_to_element(ToCity).click().send_keys_to_element(ToCity,"BOM").perform()

    time.sleep(10)