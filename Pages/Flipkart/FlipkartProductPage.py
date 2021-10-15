from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Locators.FlipkartLocators import Locators


class FlipkartProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Locators
        self._price_xpath = Locators.price_xpath
        self._add_to_cart = Locators.add_to_cart

    def get_page_title(self):
        return self.driver.title

    def get_product_price(self):
        price_element = self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, self._price_xpath)))
        return price_element[0].text

    def add_to_cart(self):
        add_to_cart = self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, self._add_to_cart)))
        add_to_cart[0].click()
