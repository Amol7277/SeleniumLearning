import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_VWO_login_error():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    email_id = driver.find_element(By.ID,"login-username")
    email_id.send_keys("admin@admin.com")

    pwd = driver.find_element(By.ID,"login-password")
    pwd.send_keys("admin")

    driver.find_element(By.ID,"js-login-btn").click()

    time.sleep(2)
    error = driver.find_element(By.ID,"js-notification-box-msg")

    assert "Your email, password, IP address or location did not match" == error.text