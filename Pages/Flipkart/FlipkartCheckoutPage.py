import time
from Pages.Locators.FlipkartLocators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FlipkartCheckoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Locators
        self._plus_button = Locators.plus_button
        self._final_amount = Locators.final_amount

    def add_quantity(self, num_of_quantity):
        plus_btn = self.driver.find_elements(By.XPATH, self._plus_button)
        for _ in range(num_of_quantity):
            plus_btn[1].click()
            time.sleep(2)

    def get_total_amount(self):
        return self.driver.find_elements(By.XPATH, self._final_amount)[0].text
