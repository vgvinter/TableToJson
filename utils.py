
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def highlight_values(value):
    def recursive_print(obj, indent=0, is_last_element=True):
        if isinstance(obj, dict):
            print("{")
            last_key = list(obj.keys())[-1]
            for key, value in obj.items():
                print(f"{' ' * (indent + 2)}{key}: ", end="")
                recursive_print(value, indent + 2, key == last_key)
            print(f"{' ' * indent}}}", end=",\n" if not is_last_element else "\n")
        elif isinstance(obj, list):
            print("[")
            for index, value in enumerate(obj):
                print(f"{' ' * (indent + 2)}", end="")
                recursive_print(value, indent + 2, index == len(obj) - 1)
            print(f"{' ' * indent}]", end=",\n" if not is_last_element else "\n")
        else:
            if isinstance(obj, str):
                obj = f'"{obj}"'
            print(colored(obj, "light_blue"), end=",\n" if not is_last_element else "\n")

    recursive_print(value)


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