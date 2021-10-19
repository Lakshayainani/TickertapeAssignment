import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def setup(headless=False):
    if headless:
        # For headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        try:
            driver = webdriver.Chrome("../utils/chromedriver.exe",chrome_options=chrome_options)
        except WebDriverException:
            time.sleep(1)
            driver = webdriver.Chrome("../utils/chromedriver.exe",chrome_options=chrome_options)
    else:
        try:
            driver = webdriver.Chrome("../utils/chromedriver.exe")
        except WebDriverException:
            time.sleep(1)
            driver = webdriver.Chrome("../utils/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    return driver, wait

def tearDown(driver):
    driver.close()
    driver.quit()