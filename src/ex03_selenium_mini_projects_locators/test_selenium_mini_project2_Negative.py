'''
## **Project 1 - Automating by using the Selenium Python. **
1. Navigate to the URL -  [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
2. Find the **Make appointment** Button
3. Click on the **Make appointment **Button
4. Next Page will be loaded
5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button
6. Verify current URL - [katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment)
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_selenium_mini_project2_Negative():
    chorme_options= Options()
    chorme_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chorme_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php")
    make_appointment = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()
    time.sleep(2)

    username = driver.find_element(By.NAME,"username")
    username.send_keys("John Doe1")
    time.sleep(2)

    password = driver.find_element(By.NAME,"password")
    password.send_keys("ThisIsNotAPassword1111")
    time.sleep(2)

    login = driver.find_element(By.ID,"btn-login")
    login.click()
    time.sleep(2)

    error = driver.find_element(By.CLASS_NAME,"text-danger")
    time.sleep(2)

    assert "Login failed! Please ensure the username and password are valid." == error.text

    time.sleep(5)