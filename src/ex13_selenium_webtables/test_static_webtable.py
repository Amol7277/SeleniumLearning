import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_StaticWebtable():
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_option)
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    userTable = driver.find_element(By.XPATH, "//h6[normalize-space()='User Table']")

    driver.execute_script("arguments[0].scrollIntoView(true);", userTable)
    time.sleep(1)

    #//table[@id='resultTable']/tbody/tr[1]/td[2]

    rows = driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr")
    totla_row = len(rows)
    print(totla_row)

    cols = driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr[1]/td")
    total_column = len(cols)
    print(total_column)

    part1 = "//table[@id='resultTable']/tbody/tr["
    part2 = "]/td["
    part3 = "]"

    for i in range(1, totla_row + 1):
        # print(i.text)
        for j in range(1, total_column + 1):
            data = f"{part1}{i}{part2}{j}{part3}"
            # print(data)
            tableData = driver.find_element(By.XPATH, data).text
            # print(tableData)

            if "Jasmine" in tableData:
                status = f"{data}/follwing-sibling::td"
                statustext = driver.find_element(By.XPATH, status).text
                print(f"the status is {statustext}")
            else:
                print("Not Found")

