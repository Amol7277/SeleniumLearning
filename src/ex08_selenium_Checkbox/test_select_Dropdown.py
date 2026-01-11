import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_selectDropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")

    dropdown = driver.find_element(By.ID,"selenium_commands")

    select = Select(dropdown)
    select.select_by_visible_text("Switch Commands")
    time.sleep(2)
    select.select_by_index(1)
    time.sleep(2)
    select.select_by_visible_text("WebElement Commands")

    time.sleep(10)