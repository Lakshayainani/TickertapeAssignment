import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Pages.Locators.AmazonLocators import Locators


class AmazonProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Locators
        self._price_id = Locators.price_id
        self._add_to_cart = Locators.add_to_cart_id
        self._cart_icon = Locators.cart_icon_id
        self._side_sheet_close = Locators.side_sheet_close

    def get_page_title(self):
        return self.driver.title

    def get_product_price(self):
        price_element = self.wait.until(ec.visibility_of_element_located((By.ID, self._price_id)))
        return price_element.text

    def add_to_cart(self):
        self.driver.find_element(By.ID, self._add_to_cart).click()
        time.sleep(4)

    def close_side_sheet(self):
        self.driver.find_element(By.ID,self._side_sheet_close).click()

    def open_cart(self):
        self.driver.find_element(By.ID,self._cart_icon).click()