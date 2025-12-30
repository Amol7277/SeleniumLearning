from selenium import webdriver
import pytest
import time
import allure


@allure.title("Print the Page Source of the page.")
def test_page_source_Edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_as_html = driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert "CURA Healthcare Service" in page_source_as_html
    time.sleep(5)
    driver.quit()

@allure.title("Print the Page Source of the page.")
def test_page_source_Chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_as_html = driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert "CURA Healthcare Service" in page_source_as_html
    time.sleep(5)
    driver.quit()

@allure.title("Print the Page Source of the page.")
def test_page_source_FireFox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_as_html = driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert "CURA Healthcare Service" in page_source_as_html
    time.sleep(5)
    driver.quit()