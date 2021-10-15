from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Locators.AmazonLocators import Locators


class AmazonCheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self._final_amount = Locators.cart_Amount

    def get_total_amount(self):
        return self.driver.find_elements(By.XPATH, self._final_amount)[0].text