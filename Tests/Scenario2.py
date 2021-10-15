from Pages.Amazon.AmazonCheckoutPage import AmazonCheckoutPage
from Pages.Amazon.AmazonHomePage import AmazonHomePage
from Pages.Amazon.AmazonProductPage import AmazonProductPage
from Pages.Flipkart.FlipkartCheckoutPage import FlipkartCheckoutPage
from Pages.Flipkart.FlipkartHomePage import FlipkartHomePage
from Pages.Flipkart.FlipkartProductPage import FlipkartProductPage
from config.config import *
from utils.driverInit import setup, tearDown

driver, wait = setup()  # driver Initialization

#### FETCHING FLIPKART PRICE ####
driver.get(flipkartURL)
flipkartHomePageHandler = driver.current_window_handle

driver.implicitly_wait(10000)
flipkartHome = FlipkartHomePage(driver)  # flipkart home object
flipkartHome.close_login_popup()  # handle login popup
flipkartHome.search_for_product(product)  # type in search bar
flipkartHome.select_first_product()  # opens a new tab

windowHandlers = driver.window_handles
driver.switch_to.window(windowHandlers[1])

flipkartProduct = FlipkartProductPage(driver)
productPageHandler = driver.current_window_handle
FLIPKART_PRICE = flipkartProduct.get_product_price()
print(f"**************\nPrice of the Product on Flipkart is : {FLIPKART_PRICE} \n**************\n")
flipkartProduct.add_to_cart()

flipkartCheckoutPage = FlipkartCheckoutPage(driver)
CHECKOUT_PRICE_FLIPKART = flipkartCheckoutPage.get_total_amount()
print(f"**************\nTotal Flipkart cart amount : {CHECKOUT_PRICE_FLIPKART} \n**************\n")

###############################
driver.switch_to.window(flipkartHomePageHandler)
driver.close()
driver.switch_to.window(productPageHandler)
#### FETCHING AMAZON PRICE ####
driver.get(amazonURL)
amazonHomePageHandler = driver.current_window_handle

amazonHome = AmazonHomePage(driver)
amazonHome.search_for_product(product)
amazonHome.select_first_product()

windowHandlers = driver.window_handles
driver.switch_to.window(windowHandlers[1])

amazonProduct = AmazonProductPage(driver)
AMAZON_PRICE = amazonProduct.get_product_price()
print(f"**************\nPrice of the Product on Amazon is : {AMAZON_PRICE} \n**************\n")

amazonProduct.add_to_cart()
amazonProduct.close_side_sheet()
amazonProduct.open_cart()

amazonCheckout = AmazonCheckoutPage(driver)
CHECKOUT_PRICE_AMAZON = amazonCheckout.get_total_amount().strip()
print(f"**************\nTotal Flipkart cart amount : {CHECKOUT_PRICE_AMAZON} \n**************\n")

tearDown(driver)
###############################
amznPrice = int("".join(ch for ch in CHECKOUT_PRICE_AMAZON.split('.')[0] if ch.isdigit()))
flpkrtPrice = int("".join(ch for ch in CHECKOUT_PRICE_FLIPKART.split('.')[0] if ch.isdigit()))

print(f"Amazon Price is {amznPrice}\nFlipkart Price is {flpkrtPrice}")

if amznPrice < flpkrtPrice:
    print(f"AMAZON IS CHEAPER BY {flpkrtPrice-amznPrice}")
else:
    print(f"FLIPKART IS CHEAPER BY {amznPrice - flpkrtPrice}")