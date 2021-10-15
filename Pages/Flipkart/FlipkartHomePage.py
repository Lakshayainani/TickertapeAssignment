from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Locators.FlipkartLocators import Locators

class FlipkartHomePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Locators
        self._search_box_class = Locators.search_box_class
        self._popup_close_button = Locators.popup_close_button
        self._search_icon = Locators.search_icon
        self._first_product_class = Locators.first_product_class
        self._first_product = Locators.first_product

    def close_login_popup(self):
        # print("waiting for login popup")
        popup_close = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, self._popup_close_button)))  # wait for the popup to be visible
        popup_close.click()  # click X to close the popup
        self.driver.implicitly_wait(3000)
        # print("pop up closed")

    def search_for_product(self, product):
        self.driver.find_element(By.CLASS_NAME, self._search_box_class).send_keys(
            product)  # enter product name in search box
        self.driver.find_element(By.CLASS_NAME, self._search_icon).click()  # click search icon
        self.driver.implicitly_wait(5000)  # wait for products to load

    def select_first_product(self):
        self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, self._first_product)))
        products = self.driver.find_elements(By.CLASS_NAME, self._first_product_class)
        products[0].click()
        self.driver.implicitly_wait(3000)
        # return productPage
