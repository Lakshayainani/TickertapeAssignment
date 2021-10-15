from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Locators.AmazonLocators import Locators

class AmazonHomePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self._search_box_id = Locators.search_box_id
        self._search_submit_button = Locators.search_submit_button_id
        self._first_product_class = Locators.product_locator_class

    def search_for_product(self,product):
        self.driver.find_element(By.ID, self._search_box_id).send_keys(product)
        self.driver.find_element(By.ID, self._search_submit_button).click()  # click search icon
        self.driver.implicitly_wait(5000)

    def select_first_product(self):
        products = self.driver.find_elements(By.XPATH,self._first_product_class)
        products[0].click()