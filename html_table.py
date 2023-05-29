from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_driver(doi, chromedriver_path):
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    url = "http://dx.doi.org/" + doi
    driver.get(url)
    return driver


def extract_tableSource(driver):
    tableSource = driver.find_elements(By.TAG_NAME, "table")
    print(tableSource)
    print(f"number of tables = {len(tableSource)}")
    return tableSource


def extract_table(tableSource, table_num):
    html_table = tableSource[table_num - 1].get_attribute("outerHTML")
    return html_table


def quit_driver(driver):
    driver.close()  # terminates the loaded browser window
    driver.quit()  # ends the webdriver application