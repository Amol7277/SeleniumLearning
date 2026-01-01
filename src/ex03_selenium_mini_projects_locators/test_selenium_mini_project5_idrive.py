import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_VWO_login_error():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(5)
    email_id = driver.find_element(By.ID,"username")
    email_id.send_keys("augtest_040823@idrive.com")

    pwd = driver.find_element(By.ID,"password")
    pwd.send_keys("123456")

    driver.find_element(By.ID,"frm-btn").click()

    time.sleep(15)

    upgrade = driver.find_element(By.ID,"upgrade")

    assert "Your free trial has expired\nUpgrade Now!" == upgrade.text