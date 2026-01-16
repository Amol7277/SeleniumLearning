import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shadowDom():
    chrome_option = Options()
    chrome_option.add_argument("--incognito")

    webdriver.Chrome()
    driver = webdriver.Chrome(chrome_option)
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(2)
    dom = driver.find_element(By.XPATH,"//h6[contains(text(),'Shadow DOM')]")

    driver.execute_script("arguments[0].scrollIntoView(true);",dom)

    time.sleep(2)

    kilsinput = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('#kils')")
    kilsinput.send_keys("Test")

    time.sleep(2)
    pizza_input = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('#pizza')")
    pizza_input.send_keys("test2")






    # shadow_host1 = driver.find_element(By.ID,"userName")
    # shadow_root1 = shadow_host1.shadow_root
    #
    # name = shadow_root1.find_element(By.ID,"kils")
    # name.send_keys("Test")
    #
    # time.sleep(2)
    #
    # shadow_host2 = shadow_root1.find_element(By.ID,"app2")
    # shadow_root2 = shadow_host2.shadow_root
    #
    # pizzaname = shadow_root2.find_element(By.ID,"pizza")
    # pizzaname.send_keys("Test")
    #
    # time.sleep(2)

    # shadow_host3 = shadow_root1.find_element(By.ID,"concepts")
    # shadow_root3 = shadow_host3.shadow_root
    # print("shadow_root3")

    # time.sleep(2)
    # Concepts = shadow_root1.find_element(By.ID,"training")
    # Concepts.send_keys("Test")

    time.sleep(5)