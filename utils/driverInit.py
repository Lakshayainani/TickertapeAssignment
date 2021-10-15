from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def setup():
    driver = webdriver.Chrome("../utils/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    wait = WebDriverWait(driver,10)
    return driver,wait

def tearDown(driver):
    driver.close()
    driver.quit()