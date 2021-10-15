from Pages.Flipkart.FlipkartCheckoutPage import FlipkartCheckoutPage
from Pages.Flipkart.FlipkartHomePage import FlipkartHomePage
from Pages.Flipkart.FlipkartProductPage import FlipkartProductPage
from config.config import *
from utils.driverInit import setup, tearDown

driver, wait = setup()  # driver Initialization
driver.get(flipkartURL)
homePageHandler = driver.current_window_handle

driver.implicitly_wait(10000)
flipkartHome = FlipkartHomePage(driver)  # flipkart home object
flipkartHome.close_login_popup()  # handle login popup
flipkartHome.search_for_product(product)  # type in search bar
flipkartHome.select_first_product()  # opens a new tab

#### handling the new tab ####
windowHandlers = driver.window_handles
driver.switch_to.window(windowHandlers[1])
####  ------------------- ####

flipkartProduct = FlipkartProductPage(driver)
productPageHandler = driver.current_window_handle
PRICE_OF_PRODUCT = flipkartProduct.get_product_price()
print(f"**************\nPrice of the Product is : {PRICE_OF_PRODUCT} \n**************\n")
flipkartProduct.add_to_cart()

flipkartCheckoutPage = FlipkartCheckoutPage(driver)
flipkartCheckoutPage.add_quantity(1)
FINAL_CART_AMOUNT = flipkartCheckoutPage.get_total_amount()
print(f"**************\nTotal cart amount : {FINAL_CART_AMOUNT} \n**************\n")

tearDown(driver)